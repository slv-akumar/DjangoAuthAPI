

from rest_framework import serializers
from .models import User, School, Class

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address']

class ClassSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField()

    class Meta:
        model = Class
        fields = ['id', 'name', 'school_id']

    def create(self, validated_data):
        school_id = validated_data.pop('school_id')
        school = School.objects.get(id=school_id)
        instance = Class.objects.create(school=school, **validated_data)
        return instance
