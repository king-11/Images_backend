from rest_framework import serializers
from .models import *
from drf_yasg.utils import swagger_serializer_method


class ImageSerializer(serializers.ModelSerializer):
    photographer_name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.person.user.first_name + obj.person.user.last_name

    class Meta:
        model = images
        fields = ('id', 'link', 'likes', 'place',
                  'tag', 'photographer_name', 'person')
        read_only_fields = ['person', 'likes']


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.user.first_name + obj.user.last_name

    class Meta:
        model = photographer
        fields = ('id', 'home', 'name', 'instituition',
                  'profile_pic', 'bio', 'gender', 'instaHandle')


class MemberSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.user.first_name + obj.user.last_name

    class Meta:
        model = photographer
        fields = ('id', 'home', 'name', 'profile_pic', 'instaHandle')
