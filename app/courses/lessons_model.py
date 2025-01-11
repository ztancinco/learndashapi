"""
Module defining the lessons model for courses.
"""

from django.db import models
from .courses_model import CoursesModel

class LessonsModel(models.Model):
    """
    Model representing a lesson in a course.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(
        CoursesModel,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField()

    class Meta:
        """
        Meta options for LessonsModel.

        Specifies the default ordering of lessons by the `order` field.
        """
        ordering = ['order']

    def __str__(self):
        """
        String representation of a LessonsModel instance.

        Returns the lesson's order and title, including the course name for context.
        """
        return f"Course: {self.course.title} - {self.order}. {self.title}"  # pylint: disable=no-member
