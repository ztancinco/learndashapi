from rest_framework import generics
from .courses_model import CoursesModel
from .courses_serializer import CourseSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = CoursesModel.objects.all()
    serializer_class = CourseSerializer
