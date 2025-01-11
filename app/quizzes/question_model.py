"""
Model for the Question.
"""

from django.db import models
from .quizzes_model import QuizModel

class QuestionModel(models.Model):
    """
    Model representing a question in a quiz.
    """
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
