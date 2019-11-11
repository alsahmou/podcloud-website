from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

from phone_field import PhoneField

# Create your models here.
class Poduser(models.Model):
    username = models.CharField(max_length=20, null=True, unique=True)
    name = models.CharField(max_length=20, null=True, unique=True)
    phone_number = models.DecimalField(decimal_places=0, null=True, max_digits=20, unique=True)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    password = models.CharField(max_length=20, null=True)
    password_confirmation = models.CharField(max_length=20, null=True)
    

class Podcast(models.Model):
    username = models.CharField(max_length=20, null=True)
    podcast_image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=20, null=True, blank=True)
    published_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

class Episode(models.Model):
    podcast_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    episode_mp3 = models.FileField(max_length=100, null=True, blank=True)
    episode_image = models.ImageField(blank=True, null=True)





