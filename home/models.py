# views.py
from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant = Restaurant.objects.first()  # Fetch the first restaurant
        return render(request, 'homepage.html', {'restaurant': restaurant})