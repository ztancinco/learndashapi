"""
Service for managing quizes.

This is a service class to handle actions related to quizzes
"""

from django.shortcuts import get_object_or_404
from ..courses.models.quiz_model import QuizModel
from ..courses.models.question_model import QuestionModel
from ..courses.serializers.quiz_serializer import QuizSerializer
from ..courses.serializers.question_serializer import QuestionSerializer


class QuizService:
    """
    Service class for handling Quiz-related operations.
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


class QuestionService:
    """
    Service class for handling Question-related operations.
    """

    @staticmethod
    def get_question_by_id(question_id):
        """
        Retrieve a question by its ID and serialize it.

        :param question_id: ID of the question to retrieve
        :return: Serialized question data
        """
        question = get_object_or_404(QuestionModel, id=question_id)
        serializer = QuestionSerializer(question)
        return serializer.data

    @staticmethod
    def get_all_questions(quiz_id):
        """
        Retrieve all questions associated with a quiz.

        :param quiz_id: ID of the quiz
        :return: Serialized list of questions
        """
        quiz = get_object_or_404(QuizModel, id=quiz_id)
        questions = QuestionModel.objects.filter(quiz=quiz)  # pylint: disable=no-member
        serializer = QuestionSerializer(questions, many=True)
        return serializer.data

    @staticmethod
    def create_question(quiz_id, data):
        """
        Create a new question for a specific quiz.

        :param quiz_id: ID of the quiz
        :param data: Dictionary containing question data
        :return: Serialized question data
        """
        quiz = get_object_or_404(QuizModel, id=quiz_id)
        data['quiz'] = quiz.id
        serializer = QuestionSerializer(quiz_id, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def update_question(question_id, data):
        """
        Update an existing question.

        :param question_id: ID of the question to update
        :param data: Dictionary containing updated question data
        :return: Serialized updated question data
        """
        question = get_object_or_404(QuestionModel, id=question_id)
        serializer = QuestionSerializer(question, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def delete_question(question_id):
        """
        Delete a question by its ID.

        :param question_id: ID of the question to delete
        """
        question = get_object_or_404(QuestionModel, id=question_id)
        question.delete()
