from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
from accounts.models import Mentor, Student
from .models import Article, Task, Audience, Submission
from .forms import TaskCreationForm, TaskSubmissionForm, TaskSubmissionGradingForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import login,logout


@login_required
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


@login_required
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


@login_required
def dashboard(request):
    """User Dashboard for posts and tasks."""
    if not Student.objects.filter(username__username=request.user).exists():
        return redirect("m_dashboard")
    student_id = Student.objects.get(username__username=request.user).student_id
    track = request.user.track
    article = Article.objects.all()
    task = Task.objects.filter(Q(audience=track) | Q(audience="General"))
    submission = Submission.objects.filter(submitted_by__username=request.user)
    total_score = sum([s.score for s in submission])
    total_weight = sum([t.weight for t in task])

    # Avoid ZeroDivivsionError for empty db or no tasks
    if total_weight == 0:
        points = 0
    else:
        points = total_score / total_weight * 100

    context = {
        "article": article,
        "task": task,
        "submission": submission,
        "total_score": total_score,
        "total_weight": total_weight,
        "points": points,
        "student_id": student_id,
    }
    return render(request, "dashboard.html", context)


def posts(request):
    """Posts."""
    article = Article.objects.all()
    context = {
        "article": article,
    }
    return render(request, "articles.html", context)


def tasks(request):
    """Tasks."""
    if not Student.objects.filter(username__username=request.user).exists():
        return redirect("create_task")
    track = request.user.track
    task = Task.objects.filter(Q(audience=track) | Q(audience="General"))
    context = {
        "task": task,
    }
    return render(request, "tasks.html", context)


@login_required
def mentors_dashboard(request):
    """Dashboard for mentors."""
    if not Mentor.objects.filter(username=request.user).exists():
        return redirect("dashboard")

    # dict comprehension to get count of students in each track
    chart_data = {
        track: Student.objects.filter(username__track=track).count()
        for track in ["BackEnd", "FrontEnd", "Design", "Mobile"]
    }
    labels = list(chart_data.keys())
    data = list(chart_data.values())

    submissions = Submission.objects.filter(
        Q(audience=request.user.track) | Q(audience="General")
    ).order_by("graded_by")

    context = {
        "submissions": submissions,
        "labels": labels,
        "data": data,
    }
    return render(request, "mentors_dashboard.html", context)


@login_required
def meet_mentors(request):
    """Meet the Mentors."""
    mentors = Mentor.objects.all()
    context = {
        "mentors": mentors,
    }
    return render(request, "meet_mentors.html", context)


@login_required
def grade_submission(request, id):
    """Grade Submissions."""
    if not Mentor.objects.filter(username=request.user).exists():
        return redirect("dashboard")

    submission = Submission.objects.get(id=id)
    form = TaskSubmissionGradingForm(instance=submission)
    if request.method == "POST":
        form = TaskSubmissionGradingForm(request.POST, instance=submission)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.graded_by = Mentor.objects.get(username=request.user)
            mentor.save()
            return redirect("m_dashboard")
    context = {
        "submission": submission,
        "form": form,
    }
    return render(request, "grade_submission.html", context)
