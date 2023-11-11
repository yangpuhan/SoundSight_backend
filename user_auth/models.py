from django.db import models

class User(models.Model):
    identity = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=64)
