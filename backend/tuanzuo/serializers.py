from django.utils import timezone
from django_filters import BooleanFilter
from django_filters.rest_framework import FilterSet
from rest_framework import serializers
from backend.user.serializers import UserAuthSerializer

from .models import (
    Skill,
    Project,
)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'logo', 'simple_description', 'grade',
                  'video_tutorial', 'text_tutorial', 'start',
                  'end', 'swiper', 'recommend')


class ProjectDetailSerializer(serializers.ModelSerializer):
    created_by = UserAuthSerializer(read_only=True)
    images = JSONSerializerField()
    skills = ProjectSerializer(many=True, read_only=True)

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
