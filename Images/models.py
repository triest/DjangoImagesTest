from django.db import models
from django.contrib.auth.models import User;
from django.conf import settings


# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30);
    date = models.DateTimeField(auto_now_add=True);
    image = models.ImageField(default='default.png', blank=True)
    def __str__(self):
        return self.title;


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=500);
    image=models.ForeignKey(Image, on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True);