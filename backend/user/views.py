import json

from django.contrib.auth import login, logout
from rest_framework.exceptions import APIException
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.views import APIView

from .models import User
from .serializers import UserAuthSerializer


class ApiUserRegisterView(
    CreateModelMixin,
    UpdateModelMixin,
    APIView
):
    def post(self, request, *args, **kwargs):
        # login
        json_data = json.loads(request.body)

        username = json_data.get('username', '')
        password = json_data.get('password', '')

        user = User.objects.filter(username=username).first()
        if user:
            raise APIException('该用户名已存在')
        if not password:
            raise APIException('密码不能为空')

        user = User.objects.create_user(username, password, username=username)

        login(request, user)

        serializer = UserAuthSerializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
        )


class ApiUserAuthView(
    CreateModelMixin,
    APIView
):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            raise APIException('未登录')

        serializer = UserAuthSerializer(user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # login
        json_data = json.loads(request.body)
        username = json_data.get('username', '')
        password = json_data.get('password', '')
        user = User.objects.filter(username=username).first()
        if not user:
            raise APIException('用户不存在')
        if not user.check_password(password):
            raise APIException('密码错误')
        login(request, user)

        serializer = UserAuthSerializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
        )

    def delete(self, request, *args, **kwargs):
        # logout
        user = request.user
        if not user.is_authenticated:
            raise APIException('未登录')

        logout(request)

        return Response(status=HTTP_204_NO_CONTENT)
