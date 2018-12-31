from django.urls import path
from .views import (
    ProjectListApiView
)


urlpatterns = [
    path(r'v1/projects', ProjectListApiView.as_view()),
]
