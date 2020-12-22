from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=300, verbose_name='موضوع')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوعات'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام کاربری')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name='مقاله')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    message = models.TextField(verbose_name='پیام')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    def __str__(self):
        return self.title


class Blog(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='موضوع')
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='تصویر')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    seen = models.IntegerField(default=0, verbose_name='بازدید')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
