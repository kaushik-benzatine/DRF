from django.db import models

# Create your models here.


def is_age_valid(value):
    if value < 18:
        raise ValueError("Age cannot be less than 18")
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[is_age_valid])
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name