from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializer import *
from .models import *
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyImages
from .filters import ImageFilter
from .paginations import ImageListPagination


class TeamView(generics.ListAPIView):
    queryset = photographer.objects.filter(member=True)
    serializer_class = MemberSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = photographer.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ImagesView(generics.ListCreateAPIView):
    queryset = images.objects.select_related(
        'person', 'person__user').prefetch_related('tag').filter(verified=True).order_by('id')
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ImageFilter
    pagination_class = ImageListPagination

    def create(self, request):
        self.request = request
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.serializer.create()
        return Response(status=status.HTTP_201_CREATED)


class ImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsOwnerOrReadOnlyImages,)
