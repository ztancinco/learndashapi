from django.db import models
from courses.courses_model import CoursesModel

class QuizModel(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='quizzes')
