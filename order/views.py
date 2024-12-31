from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def order_status(request):
    orders = Order.objects.filter(customer = request.user.customer).order_by('-order_date')
    return render(request,'order_status.html',{'orders': orders})