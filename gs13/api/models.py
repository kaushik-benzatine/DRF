from django.db import models

# Create your models here.


class Singer(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    # db_table = 'singer'
    verbose_name_plural = 'singer'
    # verbose_name = 'singer'

class Songs(models.Model):
  name = models.CharField(max_length=100)
  duration = models.IntegerField()
  singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')

  def __str__(self):
    return self.name

  class Meta:
    # db_table = 'songs'
    verbose_name_plural = 'songs'
    # verbose_name = 'songs'