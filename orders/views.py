# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
        address = models.CharField(max_length=200)

        class OpeningHours(models.Model):
            DAY_CHOICES = [
                    ('Monday', 'Monday'),
                            ('Tuesday', 'Tuesday'),
                                    ('Wednesday', 'Wednesday'),
                                            ('Thursday', 'Thursday'),
                                                    ('Friday', 'Friday'),
                                                            ('Saturday', 'Saturday'),
                                                                    ('Sunday', 'Sunday'),
                                                                        ]

                                                                            restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
                                                                                day = models.CharField(max_length=10, choices=DAY_CHOICES)
                                                                                    opening_time = models.TimeField()
                                                                                        closing_time = models.TimeField()

                                                                                            def __str__(self):
                                                                                                    return f"{self.restaurant.name} - {self.day}"
