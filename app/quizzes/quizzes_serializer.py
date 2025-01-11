"""
Serializers for the Quizzes app.

This file contains serializers for the `QuizModel`, `QuestionModel`, and 
`AnswerModel` to transform them into JSON format and handle incoming data 
for the API views.
"""

from rest_framework import serializers
from .question_serializer import QuestionSerializer
from .quizzes_model import QuizModel

class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer class for QuizModel.
    """
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        """
        Meta class to define the model and fields for the QuizSerializer.
        """
        model = QuizModel
        fields = ['id', 'title', 'course', 'questions']

    def __str__(self):
        """
        String representation of the QuizSerializer instance.

        Returns a string with the quiz's ID and title.
        """
        return f"Quiz({self.instance.id}, {self.instance.title})"
