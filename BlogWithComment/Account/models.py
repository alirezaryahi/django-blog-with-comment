from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Custom_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر')
    phone = models.IntegerField(verbose_name='تلفن')

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'مشخصات کاربر'
        verbose_name_plural = 'مشخصات کاربران'
