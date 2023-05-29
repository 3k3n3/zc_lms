from django import template
from ..models import Student, Submission

register = template.Library()


@register.filter
def user(value):
    """Get logged in user from template, student instance only."""

    """The submissions are filtered based on the logged in student
     in user(value) and compared by submissions vs task title in status(value) and score(value)"""
    global submission
    user = value
    submission = Submission.objects.filter(
        submitted_by=Student.objects.get(username=user)
    )
    return submission


@register.filter
def status(value):
    """Submission Status."""
    for s in submission:
        if value == s.submitted_for:
            return s.submission_status
    return "Not Submitted"


@register.filter
def score(value):
    """Submission Score."""
    for s in submission:
        if value == s.submitted_for:
            return s.score
    return "-"
