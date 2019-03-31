from django.utils import timezone
from django_filters import BooleanFilter
from django_filters.rest_framework import FilterSet
from rest_framework import serializers
from backend.user.serializers import AuthorSerializer

from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'logo', 'simple_description', 'grade',
                  'video_tutorial', 'text_tutorial', 'start',
                  'end', 'swiper', 'recommend')


class ProjectDetailSerializer(serializers.ModelSerializer):
    created_by = AuthorSerializer(read_only=True)

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
