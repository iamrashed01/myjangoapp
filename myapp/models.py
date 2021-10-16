from django.db import models


class User(models.Model):
    name = models.CharField(null=False, max_length=200, unique=True)
    image = models.ImageField(null=False, max_length=200, unique=True)

    def __str__(self):
        return self.name
