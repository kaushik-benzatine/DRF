
from django.urls import path
from .views import  StudentListAPIView, StudentCreateAPIView, StudentRetrive, StudentUpdate, StudentDelete, StudentListCreateAPIView, StudentRetriveUpdateAPIView, StudentRetriveUpdateDestroyAPIView
urlpatterns = [
   path('list/', StudentListAPIView.as_view(), name='student-list'),
   path('create/', StudentCreateAPIView.as_view(), name='student-create'),
   path('retrive/<int:pk>/', StudentRetrive.as_view(), name='student-retrive'),
   path('update/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
   path('delete/<int:pk>/', StudentDelete.as_view(), name='student-delete'),
   path('list-create/', StudentListCreateAPIView.as_view(), name='student-list-create'),
   path('retrive-update/<int:pk>/', StudentRetriveUpdateAPIView.as_view(), name='student-retrive-update'),
   path('retrive-update-destroy/<int:pk>/', StudentRetriveUpdateDestroyAPIView.as_view(), name='student-retrive-update-destroy'),
]
