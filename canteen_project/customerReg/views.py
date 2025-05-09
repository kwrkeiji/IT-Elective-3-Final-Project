from rest_framework import generics, permissions
from .models import CustomerReg
from .serializers import CustomerRegSerializer

class CustomerRegListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerRegSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomerReg.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerRegRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerRegSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomerReg.objects.filter(user=self.request.user)