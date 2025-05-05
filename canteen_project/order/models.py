from django.db import models
from product.models import Product

class Order(models.Model):
    MODE_CHOICES = [
        ('delivery', 'Delivery'),
        ('pick-up', 'Pick-Up'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"