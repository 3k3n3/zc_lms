# Generated by Django 4.2.1 on 2023-06-11 10:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0044_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        datetime.datetime(
                            2023,
                            6,
                            11,
                            10,
                            16,
                            23,
                            725138,
                            tzinfo=datetime.timezone.utc,
                        ),
                        message="Deadline cannot be earlier than now!",
                    )
                ]
            ),
        ),
    ]
