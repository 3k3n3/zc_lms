# Generated by Django 4.2.1 on 2023-05-27 12:03

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0024_alter_submission_submission_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="score",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=4,
                validators=[django.core.validators.MinValueValidator(0.0)],
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        datetime.datetime(
                            2023, 5, 27, 12, 3, 35, 229859, tzinfo=datetime.timezone.utc
                        ),
                        message="Deadline cannot be earlier than now!",
                    )
                ]
            ),
        ),
    ]
