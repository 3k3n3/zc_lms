# Generated by Django 4.2.1 on 2023-05-16 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0008_submission_audience_2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submission",
            name="audience_2",
        ),
    ]
