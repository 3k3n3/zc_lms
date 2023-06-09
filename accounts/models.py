from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from cities_light.models import Country, Region
from smart_selects.db_fields import ChainedForeignKey
import uuid
from cloudinary.models import CloudinaryField


class CustomUser(AbstractUser):
    TRACK = (
        ("", "Select a track"),
        ("Design", "Design"),
        ("FrontEnd", "FrontEnd"),
        ("BackEnd", "BackEnd"),
        ("Mobile", "Mobile"),
    )
    GENDER = (
        ("", "Select a gender"),
        ("Female", "Female"),
        ("Male", "Male"),
        ("Prefer not to say", "Prefer not to say"),
    )
    first_name = models.CharField(max_length=15, null=True, blank=True)
    middle_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=30, unique=True, null=True, blank=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    track = models.CharField(max_length=100, choices=TRACK)
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(65), MinValueValidator(10)],
    )
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    state = ChainedForeignKey(
        Region,
        null=True,
        blank=True,
        chained_field="country",
        chained_model_field="country",
    )
    pictures = CloudinaryField("image")
    # pictures = models.ImageField(upload_to="avatars/")


class Student(models.Model):
    EXPERIENCE_LEVEL = (
        ("None", "None"),
        ("Beginner", "Beginner"),
        ("Mid-level", "Mid-level"),
        ("Expert", "Expert"),
    )
    EMPLOYMENT_STATUS = (("Employed", "Employed"), ("Unemployed", "Unemployed"))
    username = models.OneToOneField(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE
    )
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    experience_level = models.CharField(max_length=100, choices=EXPERIENCE_LEVEL)
    employment_status = models.CharField(max_length=100, choices=EMPLOYMENT_STATUS)

    # education = models.CharField(max_length=100, choices=EDUCATION)
    # how_did_you_hear_about_us = models.CharField(max_length=100, choices=REFERRAL)
    # github = models.URLField(max_length=30, unique=True, null=True, blank=True)
    # linkedin = models.URLField(max_length=30, unique=True, null=True, blank=True)
    def __str__(self):
        return str(self.username)


class Mentor(models.Model):
    username = models.OneToOneField(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE
    )
    experience = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(60), MinValueValidator(1)],
    )

    class Meta:
        permissions = (("can_manage_all_users", "To manage all students and mentors"),)

    def __str__(self):
        return str(self.username)
