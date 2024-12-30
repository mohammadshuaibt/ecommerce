from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm
from .models import ShippingAddress
# Create your views here.
def payment_success(request):
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