"""
This module contains the model for courses in the application.

The model represents a course with fields such as the title, description, 
instructor, and the creation timestamp. The instructor is a foreign key 
reference to the custom user model, DashUserModel.
"""

from django.db import models
from ..users.dash_users_model import DashUserModel

class CoursesModel(models.Model):
    """
    A model representing a course in the application.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(DashUserModel, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) if self.title else ""
