from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tasks/", views.tasks, name="all_tasks"),
    path("posts/", views.posts, name="all_posts"),
    path("post/<int:pk>", views.read_posts, name="post"),
    path("mentors/", views.meet_mentors, name="all_mentors"),
    path("create/task/", views.create_task, name="create_task"),
    path("create/post/", views.create_post, name="create_post"),
    path("detail/task/<int:id>", views.submit_task, name="task"),
    path("mentors/dashboard/", views.mentors_dashboard, name="m_dashboard"),
    path("submit/<int:id>", views.grade_submission, name="submit"),
]
