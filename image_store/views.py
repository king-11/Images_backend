from rest_framework import generics, permissions, status, authentication
from rest_framework.response import Response

from .serializer import *
from .models import *
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyImages


class TeamView(generics.ListAPIView):
    queryset = photographer.objects.filter(member=True)
    serializer_class = MemberSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = photographer.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ImagesView(generics.ListCreateAPIView):
    queryset = images.objects.filter(verified=True)
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = images.objects.filter()
    serializer_class = ImageSerializer
    permission_classes = (IsOwnerOrReadOnlyImages,)
