from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from levelupapi.views import (
    register_user,
    login_user,
    GameTypeView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
]