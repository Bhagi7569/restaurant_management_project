# views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer
            filter_backends = [DjangoFilterBackend]
                filterset_fields = ['category__name']