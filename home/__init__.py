     <!-- templates/about.html -->

     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <title>About {{ restaurant_name }}</title>
                 </head>
                 <body>
                     <nav>
                             <a href="{% url 'homepage' %}">Home</a> | About
                                 </nav>
                                     <h1>About {{ restaurant_name }}</h1>
                                         <p>{{ restaurant_description }}</p>
                                             {% if restaurant_image %}
                                                     <img src="{{ restaurant_image }}" alt="Image of {{ restaurant_name }}">
                                                         {% endif %}
                                                         </body>
                                                         </html>
                                                                                                                                                                                 