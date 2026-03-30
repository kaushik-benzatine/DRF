

from django.urls import path
from . import views

urlpatterns = [
  path("create/", views.createStudent, name="create_student "),
  path("update/", views.updateStudent, name="update_student ")
]
