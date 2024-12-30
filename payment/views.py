from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm
from .models import ShippingAddress
# Create your views here.
def payment_success(request):
    return render(request,"payment_success.html")

@login_required
def edit_shipping_info(request):
    user = request.user
    try:
        shipping_user = ShippingAddress.objects.get(user = user)
    except:
        shipping_user = None
        
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance = shipping_user)
        if form.is_valid():
            form.save()
    else:
        form = ShippingAddressForm(instance = shipping_user)
    return render(request,'edit_shipping.html',{'form':form})