from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Custom_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        pass
