from django.contrib.auth import get_user_model
from .utils import create_auth_token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import (
    LoginSerializer, RegisterSerializer, ResponseSerializer, UserSerializer)

User = get_user_model()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, *args, **kwargs):
        pass

    def login(self):
        validated_data = self.serializer.validated_data
        self.verification_status = validated_data['is_verified']
        self.user = validated_data['user']
        self.token = create_auth_token(self.user)

    def get_response(self):
        response = ResponseSerializer({
            'user_id': self.user,
            'token': self.token,
            'verification_status': self.verification_status,
        })
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self):
        self.user = self.serializer.save()
        self.token = create_auth_token(self.user)

    def get_response(self):
        response = ResponseSerializer({
            'user_id': self.user,
            'token': self.token,
            'verification_status': self.user.verified_account.is_verified,
        })
        return Response(response.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.perform_create()

        return self.get_response()


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
