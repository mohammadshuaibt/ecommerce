from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from cart.cart import Cart
from ecommerce_app.models import Product
from order.models import Order
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm
from .models import ShippingAddress
# Create your views here.


def payment_success(request):
    '''demo one.'''
    return render(request,"payment_success.html")

@login_required
def edit_shipping_info(request):
    user = request.user
    flag = 0
    try:
        shipping_user = ShippingAddress.objects.get(user = user)
    except:
        shipping_user = None
        flag = 1

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance = shipping_user)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = user
            shipping_address.save()
            if flag == 1:
                messages.success(request, ("Shipping Address Added Successfully"))
            else:
                messages.success(request, ("Shipping Address Changed Successfully"))
            return redirect('profile')
    else:
        form = ShippingAddressForm(instance = shipping_user)
    return render(request,'edit_shipping.html',{'form':form})

@login_required
def checkout(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    total_price = cart.get_total_price()

    try:
        shipping_address = ShippingAddress.objects.get(user = request.user)
    except ShippingAddress.DoesNotExist:
        shipping_address = None
        return redirect('edit_shipping')
    
        #integrate payment module
    if request.method == 'POST':
        for item in cart_items:
            product = get_object_or_404(Product, id = item['id'])
            order = Order.objects.create(
                customer = request.user.customer,
                product = product,
                quantity = item['quantity'],
                phone = shipping_address.phone,
                address = shipping_address.address,
                status = 'Pending'
            )
            #add address and phone number to model and above
            cart.clear()
            messages.success(request, "Your Order has been placed Successfully!")
        return redirect('order_status')
    
    return render(request,'checkout.html',{
        'cart_items': cart_items,
        'total_price':total_price,
        'shipping_address': shipping_address})