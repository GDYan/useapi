from rest_framework import serializers
from .models import myuser


class Userserializers(serializers.Serializer):

    name = serializers.CharField(max_length=8)
    pwd = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return myuser.objects.create(**validated_data)