from django.shortcuts import render, redirect,get_object_or_404
from . models import Product, Category,Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cart.cart import Cart
import json
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateCustomerForm
from payment.models import ShippingAddress
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user has a corresponding Customer instance
            try:
                customer = user.customer # This will raise an error if it doesn't exist
                saved_cart = customer.cart_items
                if saved_cart:
                    convert_cart = json.loads(saved_cart)
                    cart = Cart(request)
                    for key,value in convert_cart.items():
                        product = get_object_or_404(Product, id=key)
                        cart.add(product=product,quantity=value)


            except Customer.DoesNotExist:
                # Handle the case where the customer does not exist
                messages.error(request, "Your account does not have a customer profile. Please contact support.")
                return redirect('login')
            messages.success(request, "You have been logged in")
            return redirect('index')
        else:
            messages.error(request, "There was an error, please try again")
            return redirect('login')
        
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


def ContactPage(request):
    return render(request,'contact.html')

def AboutPage(request):
    return render(request,'about.html')

def register_page(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request,user)
            messages.success(request, ("You have registered successfully"))
            return redirect('index')
        else:
            messages.success(request, ("Whoops!, There was a problem registering, Please try again"))
            return redirect('register')
    return render(request,'register.html',{'form': form})

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product': product})

def category(request, namee):
    category = Category.objects.get(name=namee)
    products = Product.objects.filter(category = category)
    return render(request, 'category.html',{'products':products, 'category': category})
    
@login_required
def profile_page(request):
    user = request.user
    try:
        customer = user.customer
        shipping_address = ShippingAddress.objects.get(user = user)
    except Customer.DoesNotExist:
        customer = None
    return render(request, 'profile.html',{'user':user, 'customer':customer, 'shipping_address':shipping_address})

@login_required
def edit_profile(request):
    user = request.user
    user_form = UpdateUserForm(request.POST or None, instance=user)
    customer = get_object_or_404(Customer, user=user)
    customer_form = UpdateCustomerForm(request.POST or None, instance=customer)

    if user_form.is_valid() and customer_form.is_valid():
        user_form.save()
        customer_form.save()

        messages.success(request, "Profile Updated Successfully")
        return redirect('profile')
    else:
        if not user_form.is_valid():
            print("User Form Errors:", user_form.errors)
        if not customer_form.is_valid():
            print("Customer Form Errors:", customer_form.errors)

    return render(request, 'updateprofile.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

@login_required
def update_password(request):
    user = request.user
    if request.method == 'POST':
        form = UpdatePasswordForm(user,request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully")
            return redirect('profile')
        
        else:
            print(form.errors)
            for error in list(form.errors.values()):
                messages.error(request,error)
            return redirect('update_password')
    else:
        form = UpdatePasswordForm(user)
    return render(request,'updatepassword.html',{'form':form})       