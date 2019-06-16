from django.contrib.auth.models import AbstractUser
from django.db import models


class TimestampModel(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(
        auto_now=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class User(AbstractUser):
    pass
