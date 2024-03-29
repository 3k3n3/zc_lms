from django import forms
from .models import Task, Submission, Article
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from tinymce.widgets import TinyMCE


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "weight", "deadline", "audience"]
        widgets = {"deadline": DateTimePickerInput(), "task": TinyMCE()}


class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["submission"]
        widgets = {"submission": TinyMCE()}


class TaskSubmissionGradingForm(forms.ModelForm):
    feedback = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Submission
        fields = ["score", "feedback"]


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["posted_by"]
