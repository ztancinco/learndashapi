"""
URLs for users
"""

from django.urls import path
from .views.users import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='user-list'),
]
