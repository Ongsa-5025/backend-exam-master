import json

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.urls import reverse
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.http import JsonResponse

from apis.models import ClassRoom
from apis.serializers import ClassRoomCreateSerializer, ClassRoomUpdateSerializer, TeacherCreateSerializer, StudentCreateSerializer
from apis.filters import ClassRoomFilter


# Create your views here.
      

class ClassRoomListAPIView(ListAPIView):
   queryset = ClassRoom.objects.all()
   serializer_class = ClassRoomCreateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = ClassRoomFilter

   def get(self, request):
      try:
        data = {'message': 'Get Data Success!'}
        school_id = request.GET.get('school_id')

        teacher_list = TeacherCreateSerializer.getAllObj(school_id).annotate(
            teacher_id = F('id'),
            teacher_first_name = F('first_name'),
            teacher_lastt_name = F('last_name'),
            teacher_gender = F('gender'),
            grade = F('class_id__grade'),
            room = F('class_id__room'),
        ).values('teacher_id', 'teacher_first_name', 'teacher_lastt_name', 'teacher_gender', 'grade', 'room')

        if teacher_list:
          data['teachet_list'] = list(teacher_list)

        student_list = StudentCreateSerializer.getAllObj(school_id).annotate(
        #   teacher_list = StringAgg(Concat('teacher__first_name', Value(' '), 'teacher__last_name'),delimiter=', ', distinct=True),
        student_id = F('id'),
        student_first_name = F('first_name'),
        student_lastt_name = F('last_name'),
        student_gender = F('gender'),
        grade = F('class_id__grade'),
        room = F('class_id__room'),
        ).values('student_id', 'student_first_name', 'student_lastt_name', 'student_gender', 'grade', 'room')

        if student_list:
          data['student_list'] = list(student_list)

        return Response(data, status=status.HTTP_200_OK)
      except Exception as e:
        data = { 'message': 'Get Data Failed!', 'error' : str(e)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

   def post(self, request):
      serializer = ClassRoomCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      

class ClassRoomAPIView(ListAPIView):
   queryset = ClassRoom.objects.all()
   serializer_class = ClassRoomUpdateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = ClassRoomFilter
      
   def put(self, request, pk=None):
      instance = ClassRoom.objects.get(id=pk)
      serializer = ClassRoomUpdateSerializer(instance=instance, data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, pk=None):
      objClassRoom = ClassRoom.objects.get(id=pk)
      if objClassRoom:
        objClassRoom.delete()
        data = {'message': 'Delete Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Delete Failed!', 'error': str('ClassRoom ID: ${pk} not found!')}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      