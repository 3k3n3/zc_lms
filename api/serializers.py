from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
from accounts.models import CustomUser, Student, Mentor

CustomUser = get_user_model()


class CustomUserSerializer(ModelSerializer):
    # pictures = serializers.ImageField(
    #     max_length=None, allow_empty_file=False, use_url=True
    # )

    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
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
            # "pictures",
            "password",
            "password2",
        ]

        def save(self):
            password = self.validated_data["password"]
            password2 = self.validated_data["password2"]

            if password != password2:
                raise serializers.ValidationError(
                    {"password": "Passwords don't match."}
                )


class StudentCreationSerializer(ModelSerializer):
    username = CustomUserSerializer()

    class Meta:
        model = Student
        # fields = "__all__"

        """
        fields = [
            "username",
            "experience_level",
            "employment_status",
        ]
        """
        # fields = "__all__"
        exclude = ["github", "linkedin"]
