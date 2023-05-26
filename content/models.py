from django.db import models
from accounts.models import CustomUser, Student, Mentor
from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError
from datetime import datetime
from django.utils import timezone
from tinymce.models import HTMLField


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    posted_by = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    # post = models.TextField()
    post = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Audience(models.Model):
    AUDIENCE = (
        ("General", "General"),
        ("Design", "Design"),
        ("FrontEnd", "FrontEnd"),
        ("BackEnd", "BackEnd"),
        ("Mobile", "Mobile"),
    )


class Task(models.Model):
    posted_by = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    task = models.TextField()
    weight = models.PositiveIntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    deadline = models.DateTimeField(
        validators=[
            MinValueValidator(
                timezone.now(), message="Deadline cannot be earlier than now!"
            )
        ],
    )
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    audience = models.CharField(
        max_length=100, choices=Audience.AUDIENCE, default="General"
    )

    def __str__(self):
        return self.title


class MaxScoreTaskValidator:
    """Validate Max Score based on Task's weight."""

    def __call__(self, value):
        """Allows an instance of the class to be called as a function."""
        max_value = self.task.weight
        if value > max_value:
            raise ValidationError(
                {"score": f"The maximum score achievable for this task is {max_value}."}
            )


class Submission(models.Model):
    STATUS = (
        # ("", "Submission status"),
        ("Submitted", "Submitted"),
        ("Not Submitted", "Not Submitted"),
    )
    submitted_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission = HTMLField()
    submitted_for = models.ForeignKey(Task, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    submission_status = models.CharField(max_length=50, choices=STATUS)
    audience = models.CharField(max_length=100, choices=Audience.AUDIENCE)
    score = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=4,
        validators=[MinValueValidator(0.0)],
    )
    feedback = models.TextField(null=True, blank=True)
    graded_by = models.ForeignKey(
        Mentor, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    graded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.submitted_for)
        # return f"{self.submitted_by} for {self.submitted_for}"

    def clean(self):
        super().clean()
        """
        Create an instance of the MaxScoreTaskValidator class,
        passing the associated Task instance (self.submitted_for) as an argument.

        Call the max_value_validator instance with the score field value (self.score).
        This performs the dynamic validation against the weight value of the associated Task instance.
        """
        if self.submitted_for_id is not None:
            max_value_validator = MaxScoreTaskValidator()
            max_value_validator.task = self.submitted_for
            max_value_validator(self.score)

    # ### check if this is redundant with views
    def save(self, *args, **kwargs):
        self.submission_status = "Submitted"
        super().save(*args, *kwargs)
