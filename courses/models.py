from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_taught')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_enrolled', blank=True)
    units = models.PositiveIntegerField(default=1)


class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_present = models.BooleanField(default=True)

