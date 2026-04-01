import io

from django.shortcuts import render
from django.views import View
from .models import Student
from .serializer import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@csrf_exempt
def createStudent(request):
  if request.method == "GET":
    st = Student.objects.all()
    serializer = StudentSerializer(st, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

  if request.method == "POST":
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    serializer = StudentSerializer(data=pythondata)
    print(f"Serializer: {serializer}")
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Created'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    # json_data = JSONRenderer().render(serializer.errors)
    print(serializer.errors)


  if request.method == "PATCH":
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    serializer = StudentSerializer(stu, data=pythondata, partial=True)
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Updated'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)

  if request.method == "DELETE":
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    print(f"Student to delete: {stu}")
    stu.delete()
    res = {'msg': 'Data Deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIView(View):
  def get(self, request):
    st = Student.objects.all()
    serializer = StudentSerializer(st, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

  def post(self, request):
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    serializer = StudentSerializer(data=pythondata)
    print(f"Serializer: {serializer}")
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Created'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    # json_data = JSONRenderer().render(serializer.errors)
    print(serializer.errors)
    return HttpResponse(JSONRenderer().render(serializer.errors), content_type='application/json', status=400)

  def patch(self, request):
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    serializer = StudentSerializer(stu, data=pythondata, partial=True)
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data Updated'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)

  def delete(self, request):
    data = request.body
    streameddata = io.BytesIO(data)
    pythondata  = JSONParser().parse(streameddata)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    print(f"Student to delete: {stu}")
    stu.delete()
    res = {'msg': 'Data Deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')