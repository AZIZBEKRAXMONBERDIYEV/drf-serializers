from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True, max_length=200)
    description = serializers.CharField(read_only=True)
    completed = serializers.BooleanField(read_only=True, default=False, allow_null=True)
    created_at = serializers.DateTimeField()
