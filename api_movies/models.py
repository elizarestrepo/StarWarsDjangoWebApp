from django.contrib import admin
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=250, unique=True)
    birth_year = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    imagen = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

