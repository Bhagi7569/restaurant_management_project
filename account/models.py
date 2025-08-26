# views.py
from django.shortcuts import render
import requests

def homepage(request):
    # Assuming an API endpoint for menu items
        api_url = 'http://localhost:8000/api/menu_items/'  # Example API URL
            try:
                    response = requests.get(api_url)
                            menu_items = response.json()
                                except requests.RequestException:
                                        menu_items = []
                                            return render(request, 'homepage.html', {'menu_items': menu_items})
# models.py
from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=6, decimal_places=2)

        class Order(models.Model):
            customer = models.ForeignKey(User, on_delete=models.CASCADE)
                order_items = models.ManyToManyField(MenuItem, through='OrderItem')
                    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
                        order_status = models.CharField(max_length=20, choices=[
                                ('pending', 'Pending'),
                                        ('preparing', 'Preparing'),
                                                ('ready', 'Ready'),
                                                        ('completed', 'Completed'),
                                                                ('canceled', 'Canceled'),
                                                                    ], default='pending')

                                                                        def __str__(self):
                                                                                return f"Order {self.id} by {self.customer.username}"

                                                                                class OrderItem(models.Model):
                                                                                    order = models.ForeignKey(Order, on_delete=models.CASCADE)
                                                                                        menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                                                                            quantity = models.PositiveIntegerField(default=1)