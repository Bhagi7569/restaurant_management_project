# serializers.py
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuItem
                    fields = ['id', 'name', 'description', 'price']
                    # views.py
                    from rest_framework import viewsets
                    from rest_framework.response import Response
                    from .models import MenuItem
                    from .serializers import MenuItemSerializer
                    from rest_framework.pagination import PageNumberPagination

                    class StandardResultsSetPagination(PageNumberPagination):
                        page_size = 10
                            page_size_query_param = 'page_size'
                                max_page_size = 1000

                                class MenuItemViewSet(viewsets.ModelViewSet):
                                    queryset = MenuItem.objects.all()
                                        serializer_class = MenuItemSerializer
                                            pagination_class = StandardResultsSetPagination

                                                def get_queryset(self):
                                                        queryset = super().get_queryset()
                                                                search_query = self.request.query_params.get('search')
                                                                        if search_query:
                                                                                    queryset = queryset.filter(name__icontains=search_query)
                                                                                            return queryset