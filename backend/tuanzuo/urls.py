from django.urls import path
from .views import (
    ProjectListApiView,
    ProjectDetailApiView,
)


urlpatterns = [
    path(r'v1/projects/', ProjectListApiView.as_view()),
    path(r'v1/projects/<int:id>/', ProjectDetailApiView.as_view()),
]
