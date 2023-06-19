from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.student_signup),
    path("", views.get_all_students),
]
