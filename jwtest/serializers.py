from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Student


class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        error_messages={'required': 'Username is required',
                        'blank': 'Username is required'}
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={'required': 'Password is required',
                        'blank': 'Password is required'}
    )


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=100,
        error_messages={'required': 'Username is required',
                        'blank': 'Username is required'}
    )
    name = serializers.CharField(
        max_length=200,
        error_messages={'required': 'Name is required',
                        'blank': 'Name is required'}
    )
    email = serializers.EmailField(
        error_messages={'required': 'Email is required',
                        'invalid': 'Enter a valid email address'}
    )
