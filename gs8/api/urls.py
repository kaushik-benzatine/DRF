
from django.urls import path
from .views import  StudentListAPIView,StudentListCreateAPIView, StudentRetrive, StudentUpdate, StudentDelete

urlpatterns = [
    path('st/', StudentListAPIView.as_view(), name='create-student'),
    path('create/', StudentListCreateAPIView.as_view(), name='list-student'),
    path('st/ret/<int:pk>/', StudentRetrive.as_view(), name='retrieve-student'),
    path('st/up/<int:pk>/', StudentUpdate.as_view(), name='update-student'),
    path('st/del/<int:pk>/', StudentDelete.as_view(), name='delete-student'),
]
