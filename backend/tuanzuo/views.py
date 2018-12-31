from rest_framework import generics, serializers
from rest_framework import permissions
from rest_framework.filters import OrderingFilter

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectListApiView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    filter_backends = (OrderingFilter,)

    ordering_fields = ('id',)
    ordering = ('-id',)

    permission_classes = (permissions.AllowAny,)
