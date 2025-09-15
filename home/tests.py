
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
        history = models.TextField()
            mission = models.TextField()

                def __str__(self):
                        return self.name