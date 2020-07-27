from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers


def create_auth_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token


def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid Credentials")
    return user
