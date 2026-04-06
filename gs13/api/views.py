from django.shortcuts import render
from .serializer import SingerSerializer, SongsSerializer
from .models import Singer, Songs
from rest_framework.response import Response
from rest_framework import viewsets

class SingerViewSet(viewsets.ModelViewSet):
  queryset = Singer.objects.all()
  serializer_class = SingerSerializer

class SongsViewSet(viewsets.ModelViewSet):
  queryset = Songs.objects.all()
  serializer_class = SongsSerializer