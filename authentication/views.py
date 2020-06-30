from django.contrib.auth import get_user_model
from .utils import create_auth_token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import (
    LoginSerializer, RegisterSerializer, ResponseSerializer)

User = get_user_model()


class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = create_auth_token(user)
            response = ResponseSerializer({'token': token})
            return Response(respomse.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token = create_auth_token(user=serializer.instance)
        response = ResponseSerializer({'token': token})
        return Response(respomse.data, status.HTTP_201_CREATED)
