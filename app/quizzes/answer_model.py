"""
Model for Answer.
"""

from django.db import models
from .question_model import QuizModel

class AnswerModel(models.Model):
    """
    Model representing an answer to a quiz question.
    """
    question = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
