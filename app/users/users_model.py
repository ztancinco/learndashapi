from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)
