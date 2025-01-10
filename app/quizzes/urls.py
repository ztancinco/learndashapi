from django.urls import path
from .quizes_list_create_view import QuizListCreateView

urlpatterns = [
    path('', QuizListCreateView.as_view(), name='quiz-list-create'),
]
