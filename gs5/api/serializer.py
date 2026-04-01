from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

    # feault added : create update
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


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['age']
        # or
        extra_kwargs = {
            'age': {'read_only': True}
        }
    def address_validator(value):
        if len(value) < 5:
            raise serializers.ValidationError("Address must be at least 5 characters long.")
        return value

    address = serializers.CharField(validators=[address_validator])
    age = serializers.IntegerField(read_only=True)

    def validate_age(self, value):
        if value < 25:
            raise serializers.ValidationError("Age must be at least 25.")
        return value

    def validate(self, data):
       if data['age'] < 30 and 'professor' in data['address'].lower():
           raise serializers.ValidationError("Professors must be at least 30 years old.")
       return data
