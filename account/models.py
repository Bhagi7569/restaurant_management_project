# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MenuItemSerializer

class MenuAPIView(APIView):
    def get(self, request):
            # Hardcoded menu data for simplicity
                    menu_data = [
                                {'name': 'Burger', 'description': 'Juicy beef burger', 'price': 8.99},
                                            {'name': 'Pizza', 'description': 'Cheese pizza with veggies', 'price': 10.99},
                                                        {'name': 'Salad', 'description': 'Fresh garden salad', 'price': 6.99},
                                                                ]
                                                                        serializer = MenuItemSerializer(menu_data, many=True)
                                                                                return Response(serializer.data)                                                                                  quantity = models.PositiveIntegerField(default=1)