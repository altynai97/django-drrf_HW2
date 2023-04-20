from rest_framework import serializers
from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.department = validated_data['department']
        return instance


class EmployeeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=30)
    birth_year = serializers.IntegerField()
    position = PositionSerializer()
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data['full_name']
        instance.birth_year = validated_data['birth_year', instance.birth_year]
        instance.position = validated_data['position']
        instance.salary = validated_data['salary']
        return instance


