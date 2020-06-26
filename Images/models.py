from django.db import models
from django.contrib.auth.models import User;
from django.conf import settings


# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30);
    image = models.TextField();
    date = models.DateTimeField(auto_now_add=True);


    def __str__(self):
        return self.title;
