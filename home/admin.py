from django.shortcuts import render

def restaurant_page(request):
    restaurant_info = {
            'description': 'A cozy place serving delicious food.',
                    'image_url': '/static/images/restaurant.jpg'
                        }
                            return render(request, 'restaurant.html', {'restaurant': restaurant_info})
                            django.urls
