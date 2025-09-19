from django.db import models
from .models import OrderStatus  # Import the OrderStatus model

class Order(models.Model):
    # Existing fields...
        status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

            # Existing methods...