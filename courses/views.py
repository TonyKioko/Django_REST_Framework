from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from .import models
from . import serializers
# Create your views here.


class ListCreateCourse(generics.ListCreateAPIView):
    queryset=models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    
class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer   

# class ListCreateCourse(APIView):
#     def get(self,request,format=None):
#         courses = models.Course.objects.all()
#         serializer=serializers.CourseSerializer(courses, many=True)
#         return Response(serializer.data)
#     def post(self,request,format=None):
#         serializer = serializers.CourseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)