from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Project
from .serializers import (
    ProjectListSerializer,
    ProjectFilterSet,
    ProjectDetailSerializer,
)


class ProjectListApiView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProjectFilterSet
    search_fields = ('name', 'simple_description')
    ordering_fields = ('id',)
    ordering = ('-id',)

    permission_classes = (permissions.AllowAny,)


class ProjectDetailApiView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Project.objects.all()

    serializer_class = ProjectDetailSerializer
