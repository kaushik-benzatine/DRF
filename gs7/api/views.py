from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.


class StudentAPIView(APIView):
  def get(self, request, pk=None, format=None):
    if pk:
      student = Student.objects.get(id=pk)
      serializer = StudentSerializer(student)
      return Response(serializer.data, status=status.HTTP_200_OK)
    data = Student.objects.all()
    print(f"data: {data}")
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    data = request.data
    print(f"data: {data}")
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None, format=None):
    data = request.data
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def patch(self, request, pk=None, format=None):
    data = request.data
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk=None, format=None):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({'msg': 'Student deleted successfully'}, status=status.HTTP_200_OK)
