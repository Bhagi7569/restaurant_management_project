from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        order_date = models.DateTimeField(auto_now_add=True)
            total_price = models.DecimalField(max_digits=10, decimal_places=2)
                # Other fields...
                from rest_framework import serializers
                from .models import Order
                from .models import OrderItem  # Assuming you have an OrderItem model

                class OrderItemSerializer(serializers.ModelSerializer):
                    class Meta:
                            model = OrderItem
                                    fields = ['id', 'product_name', 'quantity', 'price']

                                    class OrderSerializer(serializers.ModelSerializer):
                                        items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')

                                            class Meta:
                                                    model = Order
                                                            fields = ['id', 'order_date', 'total_price', 'items']