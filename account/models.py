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
