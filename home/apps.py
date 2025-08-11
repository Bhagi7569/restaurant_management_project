# views.py
from django.shortcuts import render
from django.conf import settings

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE
        return render(request, 'homepage.html', {'phone_number': phone_number})
        <h1 style="text-align: center;">Homepage</h1>
        <p style="text-align: center;">Contact us at: {{ phone_number }}</p>
        <nav style="text-align: center; margin: 20px;">
            <a href="{% url 'home' %}" style="margin: 0 10px;">Home</a>
                <a href="{% url 'restaurant_page' %}" style="margin: 0 10px;">About Our Restaurant</a>
                    <a href="{% url 'contact_us' %}" style="margin: 0 10px;">Contact Us</a>
                    </nav>
                    
