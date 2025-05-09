from django.urls import path
from .views import CustomerRegListCreateView, CustomerRegRetrieveUpdateDestroyView

urlpatterns = [
    path('', CustomerRegListCreateView.as_view(), name='CustomerReg_list_create'),
    path('<int:pk>/', CustomerRegRetrieveUpdateDestroyView.as_view(), name='CustomerReg_detail'),
]