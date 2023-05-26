from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/task/", views.create_task, name="create_task"),
    path("detail/task/<int:id>", views.submit_task, name="task"),
    path("ment", views.mentors_dashboard, name="ment"),
    path("subs/<int:id>", views.submission, name="subs"),
]
