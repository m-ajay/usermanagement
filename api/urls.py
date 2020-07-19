from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
