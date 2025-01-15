"""
Service for Users
"""

from django.shortcuts import get_object_or_404
from ..users.models.dash_user_model import DashUserModel
from ..users.serializers.user_serializer import UserSerializer

class DashUsersService:
    """
    Service class for handling user-related operations.
    """

    @staticmethod
    def get_all_users():
        """
        Retrieve all users and serialize them.
        """
        users = DashUserModel.objects.all()  # pylint: disable=no-member
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def get_user_by_id(user_id):
        """
        Retrieve a user by its ID and serialize it.

        :param user_id: ID of the user to retrieve
        :return: Serialized user data
        """
        user = get_object_or_404(DashUserModel, id=user_id)
        serializer = UserSerializer(user)
        return serializer.data

    @staticmethod
    def create_user(data):
        """
        Create a new user.

        :param data: Dictionary containing user data
        :return: Serialized user data
        """
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def update_user(user_id, data):
        """
        Update an existing user.

        :param user_id: ID of the user to update
        :param data: Dictionary containing updated user data
        :return: Serialized updated user data
        """
        user = get_object_or_404(DashUserModel, id=user_id)
        serializer = UserSerializer(user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def delete_user(user_id):
        """
        Soft delete a user by its ID.

        :param user_id: ID of the user to delete
        """
        user = get_object_or_404(DashUserModel, id=user_id)
        user.delete()
        user.save()
