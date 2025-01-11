"""
View for listing and creating courses.

This file contains the view class for handling course listing and creation 
using the `ListCreateAPIView` class from Django Rest Framework.
"""

from rest_framework import generics
from .courses_model import CoursesModel
from .courses_serializer import CoursesSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    """
    View to list all courses and create a new course.

    This view handles GET and POST requests for courses. GET returns a list of 
    courses, while POST creates a new course.
    """
    # pylint: disable=no-member
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
