
from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('st/', StudentAPIView, name='create-student'),
]
