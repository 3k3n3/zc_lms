from django.shortcuts import render, redirect
from .models import Student, Mentor
from .forms import StudentCreationForm, MentorCreationForm


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
