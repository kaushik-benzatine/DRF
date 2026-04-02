from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        print("================================")
        print(f"Base name: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print("================================")
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



# if ModelViewSet is used then we don't have to define all the methods for CRUD operations in the viewset class, it will automatically create all the CRUD operations based on the model and serializer defined in the viewset class

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # REST all CRUD auto handle with ModelViewSet(it used generic viewset)

# If readOnlyModelViewSet is used then we can only perform GET request to get all the records or a single record based on the primary key, we cannot perform POST, PUT, PATCH and DELETE requests

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
