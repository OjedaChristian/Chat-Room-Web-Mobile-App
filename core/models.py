from django.db import models
# from django.contrib.auth.models import User
# Users passwords - 8JMhan1m3kcA
# Admin password - a1f4

from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

class Topic(models.Model):  # TEMÁTICA
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):  # BLUEPRINT DE LAS PROPIEDADES DE LAS SALAS
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)  
    members = models.ManyToManyField(User, related_name='members', blank=True)
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name


class Message(models.Model):  # BLUEPRINT SISTEMA DE MENSAJERÍA EN LAS SALAS
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField() 
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        ordering = ['-updated', '-created'] 

    def __str__(self) -> str:
        return self.body[0:50]
