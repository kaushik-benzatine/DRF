from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'roll', 'city']

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Name is too short")
        return value

    def validate(self, data):
        if data['age'] < 18 and data['city'].lower() == 'new york':
            raise serializers.ValidationError("Students under 18 cannot be from New York.")
        return data
