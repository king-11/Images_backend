from django.contrib.auth import get_user_model
from .utils import create_auth_token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import (
    LoginSerializer, RegisterSerializer, ResponseSerializer, UserSerializer)

User = get_user_model()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = create_auth_token(user)
            response = ResponseSerializer({'token': token})
            return Response(response.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token = create_auth_token(user=serializer.instance)
        response = ResponseSerializer({'token': token})
        return Response(response.data, status.HTTP_201_CREATED)


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
