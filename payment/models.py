from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'ShippingAddress'

    def __str__(self):
        return f"Shipping Address - {str(self.full_name)}"
    