from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Student, Mentor

CustomUser = get_user_model()

# admin.site.register(UserChoices)
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Mentor)
