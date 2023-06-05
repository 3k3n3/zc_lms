from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.student_signup, name="student_signup"),
    path("mentorship/", views.mentor_signup, name="mentor_signup"),
]
