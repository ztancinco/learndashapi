"""
URL configuration for the courses.
"""

from django.urls import path
from ..courses.views.courses_view import CoursesView
from ..courses.views.quizzes_view import QuizzesView

urlpatterns = [
    path('courses/', CoursesView.as_view(), name='courses-list'),
    path('courses/<int:course_id>/', CoursesView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/quizzes/', QuizzesView.as_view(), name='quizzes-list'),
]
