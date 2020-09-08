from django_filters import rest_framework as filterset
from django_filters import filters
from .models import images


class ImageFilter(filterset.FilterSet):
    photographer = filters.CharFilter(
        field_name="instaHandle", lookup_expr="icontains")
    place = filters.CharFilter(field_name="place", lookup_expr="icontains")
    likes = filters.NumericRangeFilter(field_name="likes")

    class Meta:
        model = images
        fields = ('place', 'photographer', 'likes', 'person')
