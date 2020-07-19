from rest_framework import viewsets

from api.filters import UserFilter
from api.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    ordering_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
    ]


__all__ = [
    'UserViewSet',
]
