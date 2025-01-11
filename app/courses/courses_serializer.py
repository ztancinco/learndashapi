"""
Serializer for Courses.
"""

from rest_framework import serializers
from ..courses.courses_model import CoursesModel
from ..courses.lessons_serializer import LessonsSerializer

class CoursesSerializer(serializers.ModelSerializer):
    """
    Serializer for the CoursesModel.
    """
    lessons = LessonsSerializer(many=True, read_only=True)

    class Meta:
        """
        Meta class for CoursesSerializer.
        """
        model = CoursesModel
        fields = ['id', 'title', 'description', 'instructor', 'created_at', 'lessons']
