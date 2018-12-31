from backend.user.urls import urlpatterns as user_urlpatterns
from backend.tuanzuo.urls import urlpatterns as tuanzuo_urlpatterns

urlpatterns = [
]

urlpatterns += user_urlpatterns
urlpatterns += tuanzuo_urlpatterns
