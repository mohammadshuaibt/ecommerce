from django.shortcuts import render,get_object_or_404,redirect
from .models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def order_status(request):
    orders = Order.objects.filter(customer = request.user.customer).order_by('-order_date')
    return render(request,'order_status.html',{'orders': orders})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer = request.user.customer)
    if order.status == 'Pending':
        order.status = 'Cancelled'
        order.save()
        messages.success(request, "Your order has been cancelled Successfully!")
    else:
        messages.error(request, "You can only cancel pending orders.")
    return redirect('order_status')