from django.contrib.auth.models import User
from django.db import models


class VerifyCode(models.Model):
    user = models.CharField(max_length=24,
                            unique=False)
    username = models.CharField(max_length=24,
                                unique=False)
    code = models.IntegerField(default=0)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
