from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import serializers


class Student:
    dept_list = {
        'bce': 'Biochemical Engineering',
        'bme': 'Biomedical Engineering',
        'cer': 'Ceramic Engineering',
        'che': 'Chemical Engineering',
        'chy': 'Chemistry',
        'civ': 'Civil Engineering',
        'cse': 'Computer Science and Engineering',
        'ece': 'Electronics Engineering',
        'eee': 'Electrical Engineering',
        'mat': 'Mathematics and Computing',
        'mec': 'Mechanical Engineering',
        'met': 'Metallurgical Engineering',
        'min': 'Mining Engineering',
        'mst': 'Materials Science and Technology',
        'phe': 'Pharmaceutical Engineering and Technology',
        'phy': 'Physics',
        'hss': 'Humanistic Studies'
    }

    @classmethod
    def get_department_code(cls, email):
        """
        Get department code from email id
        """
        username = email.split('@')[0]
        dept_code = username.split('.')[-1][:3]
        return dept_code

    @classmethod
    def get_department(cls, email):
        """
        Get department name from email id
        """
        dept_code = cls.get_department_code(email)
        return cls.dept_list[dept_code]

    @classmethod
    def get_year(cls, email):
        """
        Get year from email id
        """
        username = email.split('@')[0]
        year = username.split('.')[-1][3:]
        return '20' + year

    @classmethod
    def verify_email(cls, email):
        """
        Verify institute email
        """
        username = email.split('@')[0]
        domain = email.split('@')[1]
        if domain not in ['itbhu.ac.in', ]:
            return False
        if '.' not in username:
            return False
        dept_code = cls.get_department_code(email)
        if dept_code not in cls.dept_list:
            return False
        return True


def create_auth_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token


def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid Credentials")
    return user
