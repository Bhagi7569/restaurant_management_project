# views.py
from django.conf import settings
from django.shortcuts import render

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
        return render(request, 'homepage.html', {'restaurant_name': restaurant_name})
        # models.py
        from django.db import models

        class Restaurant(models.Model):
            name = models.CharField(max_length=100)
                # other fields...