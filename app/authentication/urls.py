"""
URL configuration for auth.
"""
from django.urls import path
from .auth_login_view import AuthLoginView
from .auth_logout_view import AuthLogoutView
from .auth_refresh_view import AuthRefreshTokenView

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name='auth-login'),
    path('auth/logout/', AuthLogoutView.as_view(), name='auth-logout'),
    path('auth/refresh/', AuthRefreshTokenView.as_view(), name='auth-refresh'),
]
