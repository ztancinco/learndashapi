from django.urls import path
from .courses_list_create_view import CourseListCreateView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list-create'),
]
