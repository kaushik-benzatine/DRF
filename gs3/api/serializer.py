from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=100)

  def create(self, validated_data):
    return Student.objects.create(**validated_data)

  def update(self, instance, validated_data, partial=True):
    instance.name = validated_data.get('name', instance.name)
    instance.age = validated_data.get('age', instance.age)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance

  def delete(self, instance):
    instance.delete()
    return instance
