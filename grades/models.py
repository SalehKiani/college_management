from django.db import models
from django.conf import settings
from courses.models import Course


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    midterm_grade = models.FloatField(null=True, blank=True)
    final_grade = models.FloatField(null=True, blank=True)