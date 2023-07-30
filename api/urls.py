from django.urls import path
from . import views

urlpatterns = [
    # path("signup/", views.student_signup),
    path("", views.overview),
    path("students/", views.all_students),
    path("spec/", views.Spec.as_view()),
    #     path("students/mb/", views.all_students_mb),
    #     path("students/dz/", views.all_students_dz),
    #     path("students/be/", views.all_students_be),
    #     path("students/fe/", views.all_students_fe),
    #     path("student/<int:pk>", views.get_student),
]
