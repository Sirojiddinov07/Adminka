from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField()
    description = models.TextField()
    googleplay = models.CharField(max_length=255)
    appstore = models.CharField(max_length=255)


class AdImage(models.Model):
    photo = models.ImageField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()


class Region(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ads(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    photo = models.ManyToManyField(AdImage)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.IntegerField(choices=(
        (1, 'in admin'),
        (2, 'accepted'),
        (3, 'rejected'),
        (4, 'sold'),
    ), default=1)
    is_top = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=True)
    