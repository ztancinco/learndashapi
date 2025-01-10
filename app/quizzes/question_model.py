from django.db import models
from quizes.quizes_model import QuizModel

class QuestionModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
