from django.urls import path
from .users_view import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='user-list'),
]
