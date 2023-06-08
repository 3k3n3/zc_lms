from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tasks/", views.tasks, name="all_tasks"),
    path("posts/", views.posts, name="all_posts"),
    path("mentors/", views.meet_mentors, name="all_mentors"),
    path("create/task/", views.create_task, name="create_task"),
    path("detail/task/<int:id>", views.submit_task, name="task"),
    path("ment", views.mentors_dashboard, name="ment"),
    path("subs/<int:id>", views.grade_submission, name="subs"),
]
