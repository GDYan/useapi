from rest_framework import serializers
from .models import User,myuser

# class Userserializers(serializers.ModelSerializer):
#     class Meta:
#         model = myuser,
#         fields = "__all__"
class Userserializers(serializers.Serializer):

    name = serializers.CharField(max_length=8)
    pwd = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return myuser.objects.create(**validated_data)