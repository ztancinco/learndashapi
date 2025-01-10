from django.db import models
from courses.courses_model import CoursesModel 

class LessonsModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='lessons')
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField()