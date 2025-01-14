"""
Views for the Users app.

This file contains views related to user management, such as listing all users,
retrieving a single user, and updating user details.
"""
from rest_framework import generics
from ..models.dash_user_model import DashUserModel
from ..serializers.users import UserSerializer

class UsersListView(generics.ListAPIView):
    """
    View to list all users in the system.
    This view will return a list of all users serialized using the UserSerializer.
    """
    queryset = DashUserModel.objects.all()
    serializer_class = UserSerializer
