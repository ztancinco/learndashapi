"""
Service for managing quizzes.

This module provides a service class to handle actions related to quizzes, 
such as creating, updating, retrieving, and deleting quizzes.
"""

from django.shortcuts import get_object_or_404
from ..courses.models.quiz_model import QuizModel
from ..courses.serializers.quiz_serializer import QuizSerializer


class QuizService:
    """
    Service class for handling quiz-related operations.
    """

    @staticmethod
    def get_all_quizzes():
        """
        Retrieve all quizzes and serialize them.

        :return: Serialized list of quizzes
        """
        quizzes = QuizModel.objects.all()  # pylint: disable=no-member
        serializer = QuizSerializer(quizzes, many=True)
        return serializer.data

    @staticmethod
    def get_quiz_by_id(quiz_id):
        """
        Retrieve a quiz by its ID and serialize it.

        :param quiz_id: ID of the quiz to retrieve
        :return: Serialized quiz data
        """
        quiz = get_object_or_404(QuizModel, id=quiz_id)
        serializer = QuizSerializer(quiz)
        return serializer.data

    @staticmethod
    def create_quiz(data):
        """
        Create a new quiz.

        :param data: Dictionary containing quiz data
        :return: Serialized quiz data
        """
        serializer = QuizSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def update_quiz(quiz_id, data):
        """
        Update an existing quiz.

        :param quiz_id: ID of the quiz to update
        :param data: Dictionary containing updated quiz data
        :return: Serialized updated quiz data
        """
        quiz = get_object_or_404(QuizModel, id=quiz_id)
        serializer = QuizSerializer(quiz, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def delete_quiz(quiz_id):
        """
        Delete a quiz by its ID.

        :param quiz_id: ID of the quiz to delete
        """
        quiz = get_object_or_404(QuizModel, id=quiz_id)
        quiz.delete()
