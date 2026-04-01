
from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('st/', StudentAPIView.as_view(), name='create-student'),
    path('st/<int:pk>/', StudentAPIView.as_view(), name='update-student'),
]
