from rest_framework import generics, permissions, status
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
    queryset = images.objects.filter(verified=True).order_by('likes')
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = images.objects.filter(verified=True).order_by('likes')
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(pk=user_id)
        return queryset

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


class LikeUpdateView(generics.UpdateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request):
        image_id = request.data.get('image', None)
        if not image_id:
            return Response(data={"error": "Image Id is required"}, status=status.HTTP_400_BAD_REQUEST)

        instance = get_object_or_404(Likes, image__id=image_id)
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.update()
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)
