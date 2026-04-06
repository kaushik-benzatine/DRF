from django.contrib import admin

# Register your models here.

from .models import Singer, Songs

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
  list_display = ['name', 'age', 'gender']

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
  list_display = ['name', 'duration', 'singer']