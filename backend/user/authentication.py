from django.conf import settings
from rest_framework.authentication import SessionAuthentication as BaseSessionAuthentication


class SessionAuthentication(BaseSessionAuthentication):

    def enforce_csrf(self, request):
        if settings.DEBUG:
            return
        return super(SessionAuthentication, self).enforce_csrf(request)
