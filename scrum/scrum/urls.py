from django.conf.urls import include, re_path

from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router


urlpatterns = [
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
    re_path(r'^api/', include(router.urls)),
]
