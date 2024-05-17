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

from apis.models import Student
from apis.serializers import StudentCreateSerializer, StudentUpdateSerializer
from apis.filters import StudentFilter


# Create your views here.
      

class StudentListAPIView(ListAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentCreateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = StudentFilter

   def post(self, request):
      serializer = StudentCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      

class StudentAPIView(ListAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentUpdateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = StudentFilter
      
   def put(self, request, pk=None):
      instance = Student.objects.get(id=pk)
      serializer = StudentUpdateSerializer(instance=instance, data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, pk=None):
      objStudent = Student.objects.get(id=pk)
      if objStudent:
        objStudent.delete()
        data = {'message': 'Delete Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Delete Failed!', 'error': str('Student ID: ${pk} not found!')}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      