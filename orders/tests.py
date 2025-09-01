# models.py
from django.db import models

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=200)
        city = models.CharField(max_length=100)
            state = models.CharField(max_length=50)
                zip_code = models.CharField(max_length=10)

                    def __str__(self):
                            return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
