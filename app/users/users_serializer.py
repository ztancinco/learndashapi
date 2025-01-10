from rest_framework import serializers
from users.users_model import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'role', 'bio']
