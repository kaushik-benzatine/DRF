import io

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def StudentAPIView(request):
  # data = request.body
  if request.method == 'POST':
    print("POST data")
  if request.method == 'GET':
    print("GET data")
  return Response({'msg': 'Student created successfully', 'data': request.data})


  # creating student CRUD operation using api_view

@api_view(['GET', 'POST','PATCH','DELETE'])
def StudentAPIView(request, id=None):
  if request.method == 'GET':
    data = Student.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if request.method == 'POST':
    data = request.data
    print(f"data: {data}")
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'PATCH':
    data = request.data
    id = data.get('id')
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    data = request.data
    id = data.get('id')
    student = Student.objects.get(id=id)
    student.delete()

  return Response({'msg': 'Student created successfully', 'data': request.data})