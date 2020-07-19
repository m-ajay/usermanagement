import django_filters

from users.models import User


class UserFilter(django_filters.FilterSet):

    o = django_filters.OrderingFilter(fields=(
        'id',
        'email',
        'first_name',
        'last_name',
    ),)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]
