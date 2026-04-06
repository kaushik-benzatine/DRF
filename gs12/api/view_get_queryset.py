from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

class StudentList(ListAPIView):
  queryset = Student.objects.all()
  # queryset = Student.objects.filter(name="Hashnode")
  serializer_class = StudentSerializer

  def get_queryset(self):
    return Student.objects.filter(name="Hashnode")
    # if i want to pass only current user data not related to other
    # return Student.objects.filter(passed_by=self.request.user)
