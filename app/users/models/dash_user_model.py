"""
This module contains the custom user model for the application.

The custom user model extends the default Django user model and includes 
additional fields such as user roles (student, instructor, admin) and a 
biography field for additional user information.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class DashUserModel(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    
    This model adds custom fields for user roles (student, instructor, admin) 
    and a biography field for additional information about the user.
    """
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='dashusermodel_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='dashusermodel_set',
        blank=True
    )
