# admin.py
from django.contrib import admin
from .models import MenuItem, Order, OrderItem

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)# views.py
from django.shortcuts import render
import requests

def homepage(request):
    # Assuming an API endpoint for                                                                                        quantity = models.PositiveIntegerField(default=1)