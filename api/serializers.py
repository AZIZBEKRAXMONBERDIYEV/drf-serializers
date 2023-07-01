from rest_framework import serializers


class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


class UserSerializer(serializers.Serializer):
    first = serializers.CharField(max_length=64)
    last = serializers.CharField(max_length=64)
    age = serializers.IntegerField()
