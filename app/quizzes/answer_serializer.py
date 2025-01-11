"""
Serializer for Answer.
"""

from rest_framework import serializers
from .answer_model import AnswerModel

class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer class for AnswerModel.

    This serializer converts AnswerModel instances into JSON format 
    and validates incoming answer data for creating or updating answers.
    """
    class Meta:
        """
        Meta class to define the model and fields for the AnswerSerializer.

        Specifies the model being serialized (AnswerModel) and the 
        fields to include in the serialized output.
        """
        model = AnswerModel
        fields = ['id', 'text', 'is_correct']

    def __str__(self):
        """
        String representation of the AnswerSerializer instance.

        Returns a string with the answer's ID and text if available, 
        or indicates that the instance is unsaved.
        """
        if self.instance:
            return f"Answer({self.instance.id}, {self.instance.text})"
        return "Answer(unsaved instance)"
