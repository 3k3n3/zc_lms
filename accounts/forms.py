from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student, Mentor


class StudentCreationForm(UserCreationForm):
    EXPERIENCE_LEVEL = (
        ("", "Select experience level"),
        ("None", "None"),
        ("Beginner", "Beginner"),
        ("Mid-level", "Mid-level"),
        ("Expert", "Expert"),
    )
    EMPLOYMENT_STATUS = (
        ("", "Select employment status"),
        ("Employed", "Employed"),
        ("Unemployed", "Unemployed"),
    )
    experience_level = forms.ChoiceField(choices=EXPERIENCE_LEVEL)
    employment_status = forms.ChoiceField(choices=EMPLOYMENT_STATUS)

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "middle_name",
            "last_name",
            "phone",
            "gender",
            "track",
            "age",
            "country",
            "state",
        ]
        # Autofocus is set on username by default, not anymore.
        widgets = {
            "first_name": forms.TextInput(attrs={"autofocus": True}),
            "phone": forms.TextInput(attrs={"placeholder": "eg. +2347012345678"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text from from in frontend
        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None


class MentorCreationForm(UserCreationForm):
    experience = forms.IntegerField(max_value=60, min_value=1)
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "eg. +2347012345678"})
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "track",
            "age",
            "experience",
            "country",
            "state",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text from from in frontend
        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None


class StudentChangeForm(UserChangeForm):
    experience_level = forms.ChoiceField(choices=StudentCreationForm.EXPERIENCE_LEVEL)
    employment_status = forms.ChoiceField(choices=StudentCreationForm.EMPLOYMENT_STATUS)
    github = forms.URLField()
    linkedin = forms.URLField()

    class Meta:
        model = get_user_model()
        fields = "__all__"


# class CustomUserChangeorm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = "__all__"
