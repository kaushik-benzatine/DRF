
from django.urls import path, include
from .views import student_list
urlpatterns = [
  path('list/', student_list, name='student_list'),
]