from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('MANAGER', 'Manager'),
        ('PROFESSOR', 'Professor'),
        ('STUDENT', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def is_manager(self):
        return self.user_type == 'MANAGER'

    def is_professor(self):
        return self.user_type == 'PROFESSOR'

    def is_student(self):
        return self.user_type == 'STUDENT'