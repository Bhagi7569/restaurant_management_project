# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
        address = models.TextField()

            def __str__(self):
                    return