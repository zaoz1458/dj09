from distutils.command.upload import upload
import imp
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pic=models.ImageField(upload_to="user/%y/%m")
    comment=models.TextField()
    point=models.IntegerField(default=0)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return '/media/noimage.jpg'