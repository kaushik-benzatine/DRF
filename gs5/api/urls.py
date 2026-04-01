from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('st/', StudentAPIView.as_view(), name='create-student'),
]
