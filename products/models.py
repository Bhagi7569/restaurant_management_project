# models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        description = models.TextField()
            price = models.DecimalField(max_digits=10, decimal_places=2)

            # serializers.py
            from rest_framework import serializers
            from .models import MenuItem

            class MenuItemSerializer(serializers.ModelSerializer):
                class Meta:
                        model = MenuItem
                                fields = ['id',