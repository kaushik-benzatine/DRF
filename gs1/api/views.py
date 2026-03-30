from django.http import HttpResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


# Model objects - list of students

def student_list(request):
  st = Student.objects.all()
  serializer = StudentSerializer(st, many=True)
  print(serializer.data)
  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data, content_type='application/json')