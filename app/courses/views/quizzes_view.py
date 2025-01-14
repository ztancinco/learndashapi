"""
View for listing and creating quizzes.

This file contains the view class for handling quiz listing and creation.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...services.quiz_service import QuizService


class QuizzesView(APIView):
    """
    View for managing quizzes using QuizService.
    """

    def get(self, _, quiz_id=None):
        """
        Retrieve all quizzes or a single quiz by ID.
        """
        if quiz_id:
            quiz = QuizService.get_quiz_by_id(quiz_id)
            return Response(quiz, status=status.HTTP_200_OK)
        quizzes = QuizService.get_all_quizzes()
        return Response(quizzes, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new quiz.
        """
        quiz = QuizService.create_quiz(request.data)
        return Response(quiz, status=status.HTTP_201_CREATED)

    def put(self, request, quiz_id):
        """
        Update an existing quiz.
        """
        quiz = QuizService.update_quiz(quiz_id, request.data)
        return Response(quiz, status=status.HTTP_200_OK)

    def delete(self, _, quiz_id):
        """
        Delete a quiz by ID.
        """
        QuizService.delete_quiz(quiz_id)
        return Response(
            {"message": "Quiz deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
