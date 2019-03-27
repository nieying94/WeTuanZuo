from rest_framework import generics, serializers
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import BooleanFilter
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectFilterSet(FilterSet):
    future = BooleanFilter(method='start_gte_now')

    def start_gte_now(self, queryset, name, value):
        print(123)
        if value:
            return queryset.filter('start__gte', timezone.now())
        return queryset

    class Meta:
        model = Project
        fields = ['grade', 'video_tutorial', 'swiper',
                  'recommend', 'future']


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

    serializer_class = ProjectListSerializer
