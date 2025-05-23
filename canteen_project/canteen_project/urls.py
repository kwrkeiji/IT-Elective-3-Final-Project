from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/product/', include('product.urls')),
    path('api/order/', include('order.urls')),
    path('api/customerReg/', include('customerReg.urls')),
]
