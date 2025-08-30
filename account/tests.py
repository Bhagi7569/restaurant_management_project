# views.py
from django.conf import settings
from django.shortcuts import render

def homepage(request):
    restaurant_name = settings.RESTAURANT_NAME
        return render(request, 'homepage.html', {'restaurant_name': restaurant_name})
    
    