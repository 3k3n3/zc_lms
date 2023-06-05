from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import CustomUser, Student, Mentor
from .forms import StudentCreationForm, MentorCreationForm


def student_signup(request):
    """Student Signup."""
    form = StudentCreationForm()
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            student = form.save()
            Student.objects.create(
                username=student,
                experience_level=form.cleaned_data["experience_level"],
                employment_status=form.cleaned_data["employment_status"],
            )
            print("new student created")
            return redirect("profile")
        else:
            print("something went wrong")
    context = {
        "form": form,
    }
    return render(request, "registration/student.html", context)


def mentor_signup(request):
    """Mentor Signup."""
    form = MentorCreationForm()
    if request.method == "POST":
        form = MentorCreationForm(request.POST)
        if form.is_valid():
            mentor = form.save()
            Mentor.objects.create(
                username=mentor,
                experience=form.cleaned_data["experience"],
            )
            print("new mentor created")
            return redirect("profile")
        else:
            print("something went wrong")
    context = {
        "form": form,
    }
    return render(request, "registration/mentor.html", context)
