from rest_framework import serializers

from .models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'gender', 'avatar', 'is_staff')
