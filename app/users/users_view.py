from rest_framework import generics
from .users_model import UserModel
from .users_serializer import UserSerializer

class UsersListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
