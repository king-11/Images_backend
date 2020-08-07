from django.contrib.auth import get_user_model
from .utils import create_auth_token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import (
    LoginSerializer, RegisterSerializer, ResponseSerializer, UserSerializer)

User = get_user_model()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def login(self):
        validated_data = self.serializer.validated_data
        self.user = validated_data['user']
        # self.verification_status = validated_data['is_verified']
        self.token = create_auth_token(self.user)

    def get_response(self):
        response = Response({
            # 'user_id': self.user.pk,
            'token': self.token,
            # 'verification_status':self.verification_status,
            # 'is_profile_complete':self.is_profile_complete,
        })
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.login()
            return self.get_response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        self.user = serializer.save()
        self.token = create_auth_token(user=serializer.instance)

    def get_response(self):
        response = ResponseSerializer({
            'token': self.token,
            # 'verification_status':self.user.verified_account.is_verified,
        })
        return Response(response.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return self.get_response()


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
