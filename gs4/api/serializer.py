from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=100)

  def validate_name(self, value):
    if len(value) < 2:
      raise serializers.ValidationError("Name must be at least 2 characters long.")
    return value

  def validate_age(self, value):
    if value < 0:
      raise serializers.ValidationError("Age must be a positive integer.")
    return value

  def validate_roll(self, value):
    if value < 0:
      raise serializers.ValidationError("Roll must be a positive integer.")
    return value

  def validate_city(self, value):
    if len(value) < 2:
      raise serializers.ValidationError("City must be at least 2 characters long.")
    return value

  def validate(self, data):
    if data['age'] < 18 and data['city'].lower() == 'new york':
      raise serializers.ValidationError("Students under 18 cannot be from New York.")
    return data

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
