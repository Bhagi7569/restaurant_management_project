# views.py
from django.shortcuts import render

def menu_view(request):
    menu_items = [
            {'name': 'Item 1', 'price': 10.99},
                    {'name': 'Item 2', 'price': 8.99},
                            {'name': 'Item 3', 'price': 12.99},
                                ]
                                    return render(request, 'menu.html', {'menu_items': menu_items})
                                    <!-- menu.html -->
                                    <h1>Menu</h1>
                                    <ul>
                                        {% for item in menu_items %}
                                                <li>{{ item.name }} - ${{ item.price }}</li>
                                                    {% endfor %}
                                                    </ul>
                                                    