from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=100)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    seen = models.IntegerField(default=0)

    def __str__(self):
        return self.title
