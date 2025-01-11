"""
View for listing and creating quizzes.

This file contains the view class for handling quiz listing and creation 
using the `ListCreateAPIView` class from Django Rest Framework.
"""

from rest_framework import generics
from .quizzes_model import QuizModel
from .quizzes_serializer import QuizSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    """
    View to list all quizzes and create a new quiz.

    This view handles GET and POST requests for quizzes. GET returns a list of 
    quizzes, while POST creates a new quiz.
    """
    # pylint: disable=no-member
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer
