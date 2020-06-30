from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializer import *
from .models import *
from .permissions import IsOwnerOrReadOnly


class TeamView(generics.ListAPIView):
    queryset = photographer.objects.filter(member=True)
    serializer_class = MemberSerializer
    permissions = (permissions.AllowAny,)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = photographer.objects.all()
    serializer_class = ProfileSerializer
    permissions = (IsOwnerOrReadOnly,)


class ImagesView(generics.ListCreateAPIView):
    queryset = images.objects.all()
    serializer_class = ImageSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class ImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = images.objects.all()
    serializer_class = ImageSerializer
    permissions = (IsOwnerOrReadOnly,)
