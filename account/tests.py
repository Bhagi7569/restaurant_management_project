# models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        description = models.TextField()
            price = models.DecimalField(max_digits=6, decimal_places=2)
                image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
                
                    def __str__(self):
    from django.conf import settings
    from django.conf.urls.static import static
    from django.urls import path
    from . import views

    urlpatterns = [
        # ...
        ]

        if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)