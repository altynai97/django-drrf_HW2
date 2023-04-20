from datetime import datetime

from rest_framework import serializers


class Position:
    def __init__(self, name, department):
        self.name = name
        self.department = department if department else datetime.now().date()

    def __str__(self):
        return f'{self.name}-{self.department}'


class PositionSerializer(serializers.Serializer):
    name = serializers.CharField()
    department = serializers.CharField()

    def create(self, validated_data):
        return Position()

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.department = validated_data['department']
        return instance


