from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'[ID: {self.id}, name: {self.first_name} {self.last_name}]'


__all__ = [
    'User',
]
