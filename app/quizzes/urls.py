"""
URL configuration for quizzes
"""
from django.urls import path
from .quizzes_list_create_view import QuizListCreateView

urlpatterns = [
    path('', QuizListCreateView.as_view(), name='quiz-list-create'),
]
