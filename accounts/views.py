from django.shortcuts import render, redirect
from .models import Student, Mentor
from .forms import StudentCreationForm, MentorCreationForm
import random
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import get_user_model


def student_signup(request):
    """Student Signup."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = StudentCreationForm()
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            student = form.save()
            Student.objects.create(
                username=student,
                student_id="LMS" + str(random.choice(range(100000, 1000000))),
                experience_level=form.cleaned_data["experience_level"],
                employment_status=form.cleaned_data["employment_status"],
            )
            return redirect("dashboard")
    context = {
        "form": form,
    }
    return render(request, "registration/student.html", context)


def mentor_signup(request):
    """Mentor Signup."""
    if request.user.is_authenticated:
        return redirect("m_dashboard")

    form = MentorCreationForm()
    if request.method == "POST":
        form = MentorCreationForm(request.POST)
        if form.is_valid():
            mentor = form.save()
            Mentor.objects.create(
                username=mentor,
                experience=form.cleaned_data["experience"],
            )
            return redirect("m_dashboard")
    context = {
        "form": form,
    }
    return render(request, "registration/mentor.html", context)


@login_required
def user_profile(request):
    """Profile of logged in user."""
    username = request.user

    # Condition to check if logged in user is Student or Mentor
    # is_mentor = True or False (bool) is sent to template as user status
    try:
        profile = Student.objects.get(username=username)
        is_mentor = False
    except Exception:
        # if the user is not found in Students
        profile = Mentor.objects.get(username=username)
        is_mentor = True

    context = {
        "profile": profile,
        "is_mentor": is_mentor,
    }
    return render(request, "user_profile.html", context)
