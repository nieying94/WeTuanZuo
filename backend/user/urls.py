from django.urls import path
from .views import (
    ApiUserAuthView,
    ApiUserRegisterView,
)

urlpatterns = [
    path(
        r'users/register/',
        ApiUserRegisterView.as_view(),
        name='api_user_register_view'
    ),
    path(
        r'users/auth/',
        ApiUserAuthView.as_view(),
        name='api_user_auth_view'
    ),
]
