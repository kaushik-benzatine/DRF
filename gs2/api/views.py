import io
from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def createStudent(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)

        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    return HttpResponse("This is create student API")


@csrf_exempt
def updateStudent(request):
  if request.method == "POST":
      json_data = request.body
      stream = io.BytesIO(json_data)

      pythondata = JSONParser().parse(stream)
      id = pythondata.get('id')
      stu = Student.objects.get(id=id)
      serializer = StudentSerializer(stu, data=pythondata, partial=True)
      if serializer.is_valid():
          serializer.save()
          res = {'msg': 'Data Updated'}
          json_data = JSONRenderer().render(res)
          return HttpResponse(json_data, content_type='application/json')
      json_data = JSONRenderer().render(serializer.errors)
      return HttpResponse(json_data, content_type='application/json')

  return HttpResponse("This is update student API")