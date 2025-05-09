from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from canteen_project.decorators import rate_limit

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)