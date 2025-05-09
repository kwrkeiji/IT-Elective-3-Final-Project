from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from canteen_project.decorators import rate_limit

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)  # Limit to 3 requests per minute
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=5, window=60)  # Limit to 5 requests per minute
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=5, window=60)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=3, window=60)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @rate_limit(requests=3, window=60)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @rate_limit(requests=5, window=60)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @rate_limit(requests=5, window=60)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)