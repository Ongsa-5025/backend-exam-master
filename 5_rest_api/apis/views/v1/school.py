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

from apis.models import School, ClassRoom
from apis.serializers import SchoolCreateSerializer, SchoolUpdateSerializer
from apis.filters import SchoolFilter


# Create your views here.

def index(request):
  template = loader.get_template('school.html')
  school_filter = SchoolFilter(request.GET, queryset=School.objects.all())

  context = {
    'form' : school_filter.form,
    'school_list': school_filter.qs,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add_school.html')
  return HttpResponse(template.render({}, request))

def addSchool(request):
    print(request.POST)
    response_data = []
    prepareData = {}
    template = loader.get_template('add_school.html')

    prepareData = {
        'school_name': request.POST.get('school_name', None),
        'school_short_name': request.POST.get('school_short_name', None),
        'address': request.POST.get('address', None),
    }
    serializer = SchoolCreateSerializer(data=prepareData)
    if serializer.is_valid():
        objSchool = serializer.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        print('Create School Error: ', str(serializer.errors))
        return HttpResponseRedirect(reverse('add'))
      

class SchoolListAPIView(ListAPIView):
   queryset = School.objects.all()
   serializer_class = SchoolCreateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = SchoolFilter

   def post(self, request):
      serializer = SchoolCreateSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      

class SchoolAPIView(ListAPIView):
   queryset = School.objects.all()
   serializer_class = SchoolUpdateSerializer
   filter_backends = (filters.DjangoFilterBackend,)
   filterset_class = SchoolFilter
      
   def put(self, request, pk=None):
      instance = School.objects.get(id=pk)
      serializer = SchoolUpdateSerializer(instance=instance, data=request.data)
      if serializer.is_valid():
        serializer.save()
        data = {'message': 'Create Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Create Failed!', 'error': str(serializer.errors)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, pk=None):
      objSchool = School.objects.get(id=pk)
      if objSchool:
        objSchool.delete()
        data = {'message': 'Delete Success!'}
        return Response(data, status=status.HTTP_200_OK)
      else:
        data = {'message': 'Delete Failed!', 'error': str('School ID: ${pk} not found!')}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
      