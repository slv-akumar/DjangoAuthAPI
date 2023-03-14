from rest_framework import serializers
from django.contrib.auth.models import User
from .models import School, Class

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class SchoolSerializer(serializers.ModelSerializer):
    classes = serializers.StringRelatedField(many=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'classes']

class ClassSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()

    class Meta:
        model = Class
        fields = ['id', 'name', 'teacher', 'school']
