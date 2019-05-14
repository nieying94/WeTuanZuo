from rest_framework import serializers

from .models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'is_staff', 'is_superuser')
