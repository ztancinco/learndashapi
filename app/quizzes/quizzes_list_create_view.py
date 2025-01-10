from rest_framework import generics
from .question_model import QuestionModel
from .quizes_serializer import QuizSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuizSerializer
