from django.db import models
from quizes.quizes_model import QuizModel

class AnswerModel(models.Model):
    question = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
