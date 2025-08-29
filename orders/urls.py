# views.py
from django.shortcuts import render
from .models import MenuItem

def menu(request):
    menu_items = MenuItem.objects.all()
        return render(request, 'menu.html', {'menu_items': menu_items})
        <!-- menu.html -->
        <h1>Our Menu</h1>
        <ul>
            {% for item in menu_items %}
                    <li>
                                <h2>{{ item.name }}</h2>
                                            <p>{{ item.description }}</p>
                                                        <p>Price: ${{ item.price }}</p>
                                                                </li>
                                                                    {% endfor %}
                                                                    </ul>
                                                                    