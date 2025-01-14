"""
Service for managing courses.

This is a service class to handle actions related to courses
"""

from django.shortcuts import get_object_or_404
from ..courses.models.course_model import CourseModel
from ..courses.serializers.course_serializer import CourseSerializer


class CoursesService:
    """
    Service class for handling course-related operations.
    """

    @staticmethod
    def get_all_courses():
        """
        Retrieve all courses and serialize them.
        """
        courses = CourseModel.objects.all()  # pylint: disable=no-member
        serializer = CourseSerializer(courses, many=True)
        return serializer.data

    @staticmethod
    def get_course_by_id(course_id):
        """
        Retrieve a course by its ID and serialize it.

        :param course_id: ID of the course to retrieve
        :return: Serialized course data
        """
        course = get_object_or_404(CourseModel, id=course_id)
        serializer = CourseSerializer(course)
        return serializer.data

    @staticmethod
    def create_course(data):
        """
        Create a new course.

        :param data: Dictionary containing course data
        :return: Serialized course data
        """
        serializer = CourseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def update_course(course_id, data):
        """
        Update an existing course.

        :param course_id: ID of the course to update
        :param data: Dictionary containing updated course data
        :return: Serialized updated course data
        """
        course = get_object_or_404(CourseModel, id=course_id)
        serializer = CourseSerializer(course, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def delete_course(course_id):
        """
        Delete a course by its ID.

        :param course_id: ID of the course to delete
        """
        course = get_object_or_404(CourseModel, id=course_id)
        course.delete()
