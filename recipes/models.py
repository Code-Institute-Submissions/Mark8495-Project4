from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))



class Preptime(models.Model):
    "Django Model of Preparation time database"
    preptime_image = CloudinaryField("preptime", blank=True)
    title = models.CharField(max_length=250,default='placeholder', unique=True, null=True)
    slug = models.SlugField(max_length=250,default='placeholder', unique=True, null=True)

    def __str__(self):
        return self.title


class Mealtime(models.Model):
    "Django Model of Preparation time database"
    title = models.CharField(max_length=250, default='breakfast', unique=True, null=True)
    slug = models.SlugField(max_length=250, default='breakfast', unique=True, null=True)
    mealtime_image = CloudinaryField("mealtime", blank=True)

    def __str__(self):
        return self.title