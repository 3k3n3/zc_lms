# Generated by Django 4.1 on 2023-08-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0025_student_api_key"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="student_id",
            new_name="studen_id",
        ),
    ]
