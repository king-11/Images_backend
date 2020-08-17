from rest_framework import serializers
from .utils import FirebaseAPI
from .models import *

from rest_framework.exceptions import ParseError


class ResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)
    user_id = serializers.PrimaryKeyRelatedField(
        required=True, queryset=User.objects.all())
    verification_status = serializers.BooleanField()


class LoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(max_length=2400)
    provider_token = serializers.CharField(max_length=2400, required=False)

    def validate_access_token(self, access_token):
        return FirebaseAPI.verify_id_token(access_token)

    def validate(self, attrs):
        id_token = attrs.get('id_token', None)
        provider_token = attrs.get('provider_token', None)
        user = None
        if id_token:
            jwt = self.validate_access_token(id_token)
            uid = jwt['uid']
            provider = FirebaseAPI.get_provider(jwt)

            try:
                account = VerifiedAccount.objects.get(pk=uid)
            except VerifiedAccount.DoesNotExist:
                raise serializers.ValidationError('No such account exists')

            user = account.user
            # add the verification status to the validated data
            attrs['is_verified'] = account.get_verified_status()
            if provider_token:
                account.provider_token = provider_token
                account.save()
        else:
            raise ParseError('Provide access_token or username to continue.')
        # Did we get back an active user?
        if user:
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')
        else:
            raise serializers.ValidationError(
                'Unable to log in with provided credentials.')
        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.Serializer):
    id_token = serializers.CharField(max_length=2400, required=True)
    first_name = serializers.CharField(max_length=40, allow_blank=False)
    last_name = serializers.CharField(
        max_length=100, allow_blank=True, required=False)

    def validate_id_token(self, access_token):
        return FirebaseAPI.verify_id_token(access_token)

    def validate_first_name(self, name):
        if name == None or name == '':
            raise serializers.ValidationError("First Name cannot be blank")
        return name

    def get_user(self, data, jwt):
        user = User()
        uid = jwt['uid']
        email = jwt.get('email', '')
        user.username = uid
        user.email = email
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name', "")
        return user

    def save(self):
        data = self.validated_data
        jwt = data.get('id_token')
        uid = jwt['uid']
        provider = FirebaseAPI.get_provider(jwt)
        user = self.get_user(data, jwt)
        try:
            user.validate_unique()
        except Exception as e:
            raise serializers.ValidationError(detail="User already exists")
        user.save()
        account, _ = VerifiedAccount.objects.get_or_create(
            uid=uid, user=user, provider=provider)

        if provider == VerifiedAccount.AUTH_EMAIL_PROVIDER:
            account.is_verified = False
            account.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email', 'id', 'first_name', 'last_name']
