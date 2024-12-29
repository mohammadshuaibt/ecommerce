from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_page,name='cart_page'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]