from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from accounts.models import Mentor, Student
from .models import Article, Task, Audience, Submission
from .forms import TaskCreationForm, TaskSubmissionForm, TaskSubmissionGradingForm

# from django.contrib.auth.decorators import login_required


def create_task(request):
    """Create a Task."""

    """Only Mentors can create tasks."""
    if not Mentor.objects.filter(username=request.user).exists():
        return redirect("dashboard")
    track = request.user.track
    form = TaskCreationForm()
    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        if form.data["audience"] not in [track, "General"]:
            form.add_error(
                "audience", f'You can only create General or {track} tasks!"'
            )
        if form.is_valid():
            task = form.save(commit=False)
            task.posted_by = Mentor.objects.get(username=request.user)
            task.save()
            return redirect("dashboard")

    context = {
        "form": form,
    }
    return render(request, "create_task.html", context)


def submit_task(request, id):
    """Task Submission."""

    """Only Students can submit tasks and tasks can
    only be submitted once before the task deadline."""
    task = Task.objects.get(id=id)
    if (
        not Student.objects.filter(username__username=request.user).exists()
        or Submission.objects.filter(
            submitted_for=task,
            submission_status="Submitted",
            submitted_by__username=request.user,
        ).exists()
        or task.deadline < timezone.now()
    ):
        return redirect("dashboard")

    form = TaskSubmissionForm()

    if request.method == "POST":
        form = TaskSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_for = task
            submission.submitted_by = Student.objects.get(username=request.user)
            # submission.submission_status = "Submitted" ###
            submission.audience = task.audience
            submission.save()
            return redirect("dashboard")
    context = {
        "form": form,
        "task": task,
    }
    return render(request, "submission.html", context)


def dashboard(request):
    """User Dashboard for posts and tasks."""
    if not Student.objects.filter(username__username=request.user).exists():
        return redirect("ment")
    track = request.user.track
    article = Article.objects.all()
    task = Task.objects.filter(Q(audience=track) | Q(audience="General"))

    context = {
        "article": article,
        "task": task,
    }
    return render(request, "dashboard.html", context)


def mentors_dashboard(request):
    """Dashboard for mentors."""
    submissions = Submission.objects.filter(
        Q(audience=request.user.track) | Q(audience="General")
    )
    context = {
        "submissions": submissions,
    }
    return render(request, "mentors_dashboard.html", context)


##Add only menor access
def submission(request, id):
    submission = Submission.objects.get(id=id)
    form = TaskSubmissionGradingForm(instance=submission)
    if request.method == "POST":
        form = TaskSubmissionGradingForm(request.POST, instance=submission)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.graded_by = Mentor.objects.get(username=request.user)
            mentor.save()
            return redirect("ment")
    context = {
        "submission": submission,
        "form": form,
    }
    return render(request, "subs.html", context)
