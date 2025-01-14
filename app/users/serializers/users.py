"""
Serializers for the Users app.

This file contains serializers that transform User objects into JSON 
and vice versa for use in API views. The UserSerializer handles 
serialization of the UserModel for use in user-related API operations.
"""

from rest_framework import serializers
from ..models.dash_user_model import DashUserModel

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserModel.

    This serializer is used to convert User objects to JSON format and 
    validate incoming data for user-related API operations.
    """
    class Meta:
        """
        Meta class to define the model and fields to be serialized.

        The model is UserModel, and the fields include id, username, email, 
        role, and bio.
        """
        model = DashUserModel
        fields = ['id', 'username', 'email', 'role', 'bio']
        