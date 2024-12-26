from django.shortcuts import render, redirect   
from . models import Product
from django.contrib.auth import authenticate, login, logout
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
            return redirect('index')
        else:
            return redirect('login')
        
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def ContactPage(request):
    return render(request,'contact.html')

def AboutPage(request):
    return render(request,'about.html')