"""
This file contains the quiz model
"""

from django.db import models
from ..courses.courses_model import CoursesModel

class QuizModel(models.Model):
    """
    Model representing a quiz.
    """
    title = models.CharField(max_length=255)
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='quizzes')
