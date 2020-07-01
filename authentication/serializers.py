from rest_framework import serializers
from .utils import create_auth_token, get_and_authenticate_user
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from drf_yasg.utils import swagger_serializer_method

User = get_user_model()


class ResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username and password:
            user = get_and_authenticate_user(username, password)
            if not user.is_active:
                error = "User account is disabled"
                raise serializers.ValidationError(error)
            data['user'] = user
            return data
        else:
            error = 'Must include username and password'
            raise serializers.ValidationError(error)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'required': True, 'style': {'input_type': 'password'}},
            'username': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name', required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'username']
        read_only_fields = fields
