from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Student, Mentor

CustomUser = get_user_model()
# extend a user admin class

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Mentor)
