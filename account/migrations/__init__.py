# context_processors.py
from datetime import datetime

def restaurant_info(request):
    return {
            'restaurant_name': 'Your Restaurant Name',
                    'current_year': datetime.now().year,
                        }
                                                