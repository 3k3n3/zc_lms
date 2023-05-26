from django import template
from ..models import Task, Student, Submission

register = template.Library()


@register.filter
def user(value):
    """Get logged in user from template, student instance only."""
    global user
    user = value
    return user


@register.filter
def status(value):
    """Get Task instance and compare with instances in Submission."""

    """The submissions are filtered based on the logged in student
     in user(value) and compared by submissions vs task title in status(value)"""
    submission = Submission.objects.filter(
        submitted_by=Student.objects.get(username=user)
    )
    for s in submission:
        if value == s.submitted_for:
            return "Submitted"
    return "Not Submitted"
