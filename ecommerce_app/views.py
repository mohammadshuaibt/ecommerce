from django.shortcuts import render, redirect   
from . models import Product, Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm
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
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('index')
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect('login')
        
    return render(request,'login.html')

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
    return render(request, 'profile.html',{'user':user})

@login_required
def edit_profile(request):
    user = request.user
    user_form = UpdateUserForm(request.POST or None, instance=user)

    if user_form.is_valid():
        user_form.save()

        login(request,user)
        messages.success(request, "User Updated Successfully")
        return redirect('profile')
    
    return render(request,'updateprofile.html',{'user_form': user_form})
        