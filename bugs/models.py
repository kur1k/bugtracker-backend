from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('developer', 'Разработчик'),
        ('tester', 'Тестировщик'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='tester')

class Bug(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_confidential = models.BooleanField(default=False)

    def __str__(self):
        return self.title