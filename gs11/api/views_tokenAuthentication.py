# TokenAuthentication :

# INSTALLED_APPS = [
#     'rest_framework.authtoken',
# ]

# - Generate token for a user :

    # - usign admin panel,
    # - using shell command : python manage.py drf_create_token <username>,
    # - using API endpoint : /api-token-auth/ (you have to define this endpoint in the urls.py file)
    # - using signals : we can create a token for a user automatically when the user is created by using signals.

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from .tokenauth_gen_endpoints import CustomAuthToken
from .auth_custom import CustomAuthToken


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    # authentication_classes = [CustomAuthToken] # using API endpoint for token authentication
    # permission_classes = [IsAuthenticated, IsAdminUser]
    # permission_classes = [IsAuthenticated]

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthToken] # using API endpoint for token authentication
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
