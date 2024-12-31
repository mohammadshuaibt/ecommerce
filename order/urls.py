from django.urls import path
from . import views

urlpatterns = [
    path('order_status/',views.order_status, name = 'order_status'),
    path('cancel_order<int:order_id>/',views.cancel_order,name = 'cancel_order'),
]