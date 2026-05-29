from django.db import models


class Bug(models.Model):

    title = models.CharField(max_length=255)

    status = models.CharField(max_length=100)

    priority = models.CharField(max_length=100)

    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title