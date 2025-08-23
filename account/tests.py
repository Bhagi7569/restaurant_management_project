# context_processors.py
from datetime import datetime

def restaurant_info(request):
    return {
            'restaurant_name': 'Your Restaurant Name',
                    'current_year': datetime.now().year,
                            'opening_hours': 'Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm',
                                }
<!-- base.html -->
<footer>
    <p>&copy; {{ current_year }} {{ restaurant_name }}. All rights reserved.</p>
        <p>Opening Hours: {{ opening_hours }}</p>
        </footer>
        
