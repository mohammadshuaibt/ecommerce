from django.urls import path
from . import views

urlpatterns = [
    path('payment_success/',views.payment_success,name = 'payment_success'),
    path('editshipping/',views.edit_shipping_info,name = 'edit_shipping'),
    path('checkout/', views.checkout,name = 'checkout'),
]