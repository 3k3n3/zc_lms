from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# from django.contrib.auth import get_user_model
from accounts.models import CustomUser, Student, Mentor


class CustomUserSerializer(ModelSerializer):
    pictures = serializers.ImageField(
        max_length=None, allow_empty_file=False, use_url=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "track",
            "age",
            "country",
            "state",
            "pictures",
        ]


class StudentSerializer(ModelSerializer):
    username = CustomUserSerializer()

    class Meta:
        model = Student
        fields = [
            "student_id",
            "username",
            "uid",
            "experience_level",
            "employment_status",
            "github",
            "linkedin",
        ]
