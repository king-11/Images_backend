from django_filters import rest_framework as filterset
from django_filters import filters
from .models import images


class ImageFilter(filterset.FilterSet):
    photographer_handle = filters.CharFilter(
        field_name="person__instaHandle", lookup_expr="icontains")
    place = filters.CharFilter(field_name="place", lookup_expr="icontains")
    photographer_id = filters.CharFilter(field_name="person__id")
    tags = filters.CharFilter(method='filter_tags')

    class Meta:
        model = images
        fields = ['place', 'photographer_handle',
                  'photographer_id', 'tags']

    def filter_tags(self, queryset, name, value):
        tags = value.split(",")
        return queryset.filter(tag__name__in=tags)
