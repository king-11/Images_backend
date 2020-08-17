from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        exclude = ('id',)


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.user.first_name + obj.user.last_name

    class Meta:
        model = photographer
        fields = ('id', 'home', 'name', 'instituition',
                  'profile_pic', 'bio', 'gender', 'instaHandle')


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.user.first_name + obj.user.last_name

    class Meta:
        model = photographer
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    photographer_name = serializers.SerializerMethodField('get_name')
    person = PersonSerializer(required=False)
    tag = TagSerializer(many=True, required=False)

    def get_name(self, obj):
        return obj.person.user.first_name + obj.person.user.last_name

    class Meta:
        model = images
        fields = '__all__'
        read_only_fields = ['person', 'id',
                            'photographer_name', 'likes', 'verified']

    def update(self, instance, validated_data):
        tag_list = validated_data.pop('tag', [])

        for data in validated_data:
            setattr(instance, data, validated_data[data])

        for tag_val in tag_list:
            tag_val, _ = tag.objects.get_or_create(**tag_val)
            instance.tag.add(tag_val)

        instance.save()
        return instance

    def create(self):
        tag_list = self.validated_data.pop('tag', [])
        data = self.validated_data

        data['person'] = self.context['request'].user.photographer
        image = images.objects.create(**data)
        for tag_val in tag_list:
            tag_val, _ = tag.objects.get_or_create(**tag_val)
            image.tag.add(tag_val)
        image.save()
        return image


class MemberSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj):
        return obj.user.first_name + obj.user.last_name

    class Meta:
        model = photographer
        fields = ('id', 'home', 'name', 'profile_pic', 'instaHandle')
