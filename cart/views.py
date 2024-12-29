from django.shortcuts import render, redirect, get_object_or_404
from ecommerce_app.models import Product
from .cart import Cart

# Create your views here.
def cart_page(request):
    cart = Cart(request)
    cart_items = cart.get_items()  # Get items with total price
    total_price = cart.get_total_price()  # Calculate total price for the cart

    return render(request, 'cartpage.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    return redirect('cart_page')  # Redirect to the cart page after adding

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)  # Call the remove method
    return redirect('cart_page')  # Redirect back to the cart page

def update_cart(request, product_id):
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.update(product_id,quantity)
    return redirect('cart_page')

def count(self):
    '''Returns the total number of unique items in the Cart.'''
    return len(self.cart)