from rest_framework import serializers

from .models import Task
from datetime import datetime


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False, allow_null=True)

    def create(self, validated_data):
        return Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            completed=validated_data['completed']
        )
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'completed': instance.completed,
            'created_at': instance.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
