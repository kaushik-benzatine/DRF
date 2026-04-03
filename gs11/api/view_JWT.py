from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from .tokenauth_gen_endpoints import CustomAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication] # using API endpoint for token authentication
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]



# Custom JWT fields

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView\
# # Serializer.py
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['email'] = user.email
#         token['is_admin'] = user.is_staff
#         # You can add any field from your user model here

#         return token


# # View.py
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# #url
# from django.urls import path
# from .views import MyTokenObtainPairView

# urlpatterns = [
#     # Replace the default TokenObtainPairView
#     path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # ... your other urls
# ]