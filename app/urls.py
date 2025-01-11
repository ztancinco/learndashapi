"""
URL configuration for the Learndash app.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app.users.urls')),
    path('courses/', include('app.courses.urls')),
    path('quizzes/', include('app.quizzes.urls')),
]
