from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    # password = serializers.CharField(max_length=80)
    password = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    image = serializers.URLField(max_length=200)
    bio = serializers.CharField(max_length=1000)
    phone = serializers.CharField(max_length=13)
    location = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = validated_data.get('location', instance.location)

        instance.save()
        return instance