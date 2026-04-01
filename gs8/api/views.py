from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class StudentListAPIView(GenericAPIView, ListModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
class StudentListCreateAPIView(GenericAPIView, CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

class StudentDelete(GenericAPIView, DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)



  # or
class StudentListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)


class StudentRetriveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)