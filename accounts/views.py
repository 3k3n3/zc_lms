from django.shortcuts import render, redirect
from .models import Student, Mentor, CustomUser
from .forms import LoginForm, StudentCreationForm, MentorCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def loginpage(request):
    """Login page."""
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # change entered username to lowercase since
            # usernames are always saved in lowercase.
            user = authenticate(
                username=form.cleaned_data["username"].lower(),
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.add_message(
                    request, messages.ERROR, "Invalid Username or Password"
                )

    context = {
        "form": form,
    }
    return render(request, "registration/login.html", context)


def student_signup(request):
    """Student Signup."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = StudentCreationForm()
    if request.method == "POST":
        form = StudentCreationForm(request.POST)

        # Validate unique username
        username = form.data["username"].lower()
        if CustomUser.objects.filter(username=form.data["username"]).exists():
            pass  # Allow django default error message
        elif CustomUser.objects.filter(username=username).exists():
            form.add_error("username", "A user with this username already exists.")

        # Validate unique email
        email = form.data["email"].lower()
        if CustomUser.objects.filter(email=form.data["email"]).exists():
            pass  # Allow django default error message
        elif CustomUser.objects.filter(email=email).exists():
            form.add_error("email", "A user with this email exists.")

        if form.is_valid():
            user = form.save(commit=False)
            user.username = username.lower()  # save usernames in lowercase
            user.save()
            Student.objects.create(
                username=user,
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

        # Validate unique username
        username = form.data["username"].lower()
        if CustomUser.objects.filter(username=form.data["username"]).exists():
            pass  # Allow django default error message
        elif CustomUser.objects.filter(username=username).exists():
            form.add_error("username", "A user with this username already exists.")

        # Validate unique email
        email = form.data["email"].lower()
        if CustomUser.objects.filter(email=form.data["email"]).exists():
            pass  # Allow django default error message
        elif CustomUser.objects.filter(email=email).exists():
            form.add_error("email", "A user with this email exists.")

        if form.is_valid():
            user = form.save(commit=False)
            user.username = username.lower()
            user.save()
            Mentor.objects.create(
                username=user,
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
