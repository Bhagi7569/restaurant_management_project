# home/serializers.py
from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuCategory
                    fields = ['id', 'name']
                    # home/views.py
                    from rest_framework import generics
                    from .models import MenuCategory
                    from .serializers import MenuCategorySerializer

                    class MenuCategoryList(generics.ListAPIView):
                        queryset = MenuCategory.objects.all()
                            serializer_class = MenuCategorySerializer
                                                                                 ALLOWED_HOSTS = ['yourdomain.com', 'localhost']