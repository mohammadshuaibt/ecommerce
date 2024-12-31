from django.db import models
from django.contrib.auth.models import User
from ecommerce_app.models import Customer, Product
from payment.models import ShippingAddress

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled','Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.EmailField(default="example@example.com")
    phone = models.CharField(max_length=20,default=123123123)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer.user.username} - {self.product.name}"