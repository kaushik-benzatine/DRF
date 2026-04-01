from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,  ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

class StudentListAPIView(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentCreateAPIView(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrive(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDelete(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentListCreateAPIView(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetriveUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer



# or


class StudentListCreateAPIView(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetriveUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer