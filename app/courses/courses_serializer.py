from rest_framework import serializers
from .courses_model import CoursesModel
from .lessons_model import LessonsModel

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsModel
        fields = ['id', 'title', 'content', 'video_url', 'order']

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = CoursesModel
        fields = ['id', 'title', 'description', 'instructor', 'created_at', 'lessons']
