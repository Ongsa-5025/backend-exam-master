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

from apis.models import Teacher
from apis.serializers import TeacherCreateSerializer, TeacherUpdateSerializer
from apis.filters import TeacherFilter


# Create your views here.
      

class TeacherListAPIView(ListAPIView):
   queryset = Teacher.objects.all()
   serializer_class = TeacherCreateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = TeacherFilter

   def post(self, request):
      serializer = TeacherCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      

class TeacherAPIView(ListAPIView):
   queryset = Teacher.objects.all()
   serializer_class = TeacherUpdateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = TeacherFilter
      
   def put(self, request, pk=None):
      instance = Teacher.objects.get(id=pk)
      serializer = TeacherUpdateSerializer(instance=instance, data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, pk=None):
      objTeacher = Teacher.objects.get(id=pk)
      if objTeacher:
        objTeacher.delete()
        data = {'message': 'Delete Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Delete Failed!', 'error': str('Teacher ID: ${pk} not found!')}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      