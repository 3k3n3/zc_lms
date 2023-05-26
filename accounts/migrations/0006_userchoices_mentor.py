# Generated by Django 4.2.1 on 2023-05-15 17:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
        ("accounts", "0005_student_employment_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserChoices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Female", "Female"),
                            ("Male", "Male"),
                            ("Prefer not to say", "Prefer not to say"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "track",
                    models.CharField(
                        choices=[
                            ("Design", "Design"),
                            ("FrontEnd", "FrontEnd"),
                            ("BackEnd", "BackEnd"),
                            ("Mobile", "Mobile"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mentor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_Name", models.CharField(blank=True, max_length=15, null=True)),
                ("middle_Name", models.CharField(blank=True, max_length=15, null=True)),
                ("last_Name", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=35, null=True, unique=True
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
                (
                    "track",
                    models.CharField(
                        choices=[
                            ("Design", "Design"),
                            ("FrontEnd", "FrontEnd"),
                            ("BackEnd", "BackEnd"),
                            ("Mobile", "Mobile"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Female", "Female"),
                            ("Male", "Male"),
                            ("Prefer not to say", "Prefer not to say"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "age",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(65),
                        ],
                    ),
                ),
                (
                    "experience",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(1),
                            django.core.validators.MinValueValidator(65),
                        ],
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cities_light.country",
                    ),
                ),
                (
                    "state",
                    smart_selects.db_fields.ChainedForeignKey(
                        blank=True,
                        chained_field="country",
                        chained_model_field="country",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cities_light.region",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
