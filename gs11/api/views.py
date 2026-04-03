from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
  pass

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, IsAdminUser]

    # if want to Global level authentication and permission then we can define it in the settings.py file
#     REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.IsAdminUser',
#     ],
# }

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]

#     # you can overeide global level permission by defining it in the viewset class
#     permission_classes = [AllowAny]

# ======================================================================================================



# authentication & Permission in function

# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# @api_view(['GET', 'POST','PATCH','DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def StudentAPIView(request, id=None):
#   if request.method == 'GET':
#     data = Student.objects.all()
#     serializer = StudentSerializer(data, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

#   if request.method == 'POST':
#     data = request.data
#     print(f"data: {data}")
#     serializer = StudentSerializer(data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   if request.method == 'PATCH':
#     data = request.data
#     id = data.get('id')
#     student = Student.objects.get(id=id)
#     serializer = StudentSerializer(student, data=data, partial=True)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   if request.method == 'DELETE':
#     data = request.data
#     id = data.get('id')
#     student = Student.objects.get(id=id)
#     student.delete()

#   return Response({'msg': 'Student created successfully', 'data': request.data})

# =====================================================================================================

# Remaining all permission

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     permission_classes = [IsAuthenticatedOrReadOnly]


    # FOR THIS you has to define the permissions for the user in the admin panel
    # permission_classes = [DjangoModelPermissions]

    # FOR THIS you has to define the permissions for the user in the admin panel and it will allow unauthenticated users to access the view for safe methods (GET, HEAD, OPTIONS)
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # FOR THIS you has to define the permissions for the user in the admin panel and it will allow access to the view based on the user's object permissions.
    # permission_classes = [DjangoObjectPermissions]


# ======================================================================================================

# - Custom Permission : we can create our own custom permission class by inheriting from the BasePermission class and implementing the has_permission() and has_object_permission() methods.

# from rest_framework.permissions import BasePermission
# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
#         if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
#             return True
#         return request.user and request.user.is_staff

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAdminOrReadOnly]