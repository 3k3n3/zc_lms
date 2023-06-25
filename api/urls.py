from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.student_signup),
    path("", views.overview),
    path("all/students/", views.all_students),
    path("all/students/mb/", views.all_students_mb),
    path("all/students/dz/", views.all_students_dz),
    path("all/students/be/", views.all_students_be),
    path("all/students/fe/", views.all_students_fe),
    path("get/student/<int:pk>", views.get_student),
]
