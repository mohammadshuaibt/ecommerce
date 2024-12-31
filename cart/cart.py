from django.conf import settings
from ecommerce_app.models import Customer
from payment.models import ShippingAddress
import json

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    # def db_add(self,product, quantity):
    #     product_id = str(product)
    #     product_qty = str(quantity)
    #     if product_id in self.cart:
    #         self.cart[product_id]['quantity'] += product_qty
    #     else:
    #         self.cart[product_id] = {'quantity': product_qty, 'price': str(product.price), 'name': product.name, 'image': product.image.url}
    #     self.save()
    #     self.update_cart_items()

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url}
        self.save()
        self.update_cart_items()
        self.request.session['cart'] = self.cart
        # else: 
        #     print("no customer found")

    def remove(self, product_id):
        """Remove a product from the cart."""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            self.update_cart_items()
            self.request.session.pop('cart', product_id)

    def update(self,product_id,quantity):
        '''Update the quantity of a product in Cart.'''
        product_id = str(product_id)
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.remove(product_id)
            self.save()
            self.update_cart_items()

    def update_cart_items(self):
        """Update the cart items in the database for the authenticated user."""
        if self.request.user.is_authenticated:
            current_user = Customer.objects.filter(user__id=self.request.user.id)
            cartt = {str(product_id): item['quantity'] for product_id, item in self.cart.items()}
            current_user.update(cart_items=json.dumps(cartt))

    def save(self):
        self.session.modified = True

    def get_items(self):
        """Return the items in the cart with their total price."""
        items = []
        for product_id, item in self.cart.items():
            total_price = float(item['price']) * item['quantity']
            items.append({
                'id': product_id,
                'name': item['name'],
                'image': item['image'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total_price': total_price  # Calculate total price for each item
            })
        return items

    def get_total_price(self):
        total = 0
        for item in self.cart.values():
            total += float(item['price']) * item['quantity']
        return total

    def count(self):
        """Return the total number of unique items in the cart."""
        return len(self.cart)  # Count the number of unique product IDs in the cart
    
    # def load_cart_for_user(user):
    #     if user.is_authenticated:
    #         # Load the cart items from the database
    #         shipping_address = ShippingAddress.objects.get(user=user)
    #         cart_items = json.loads(shipping_address.cart_items)  # Assuming you store cart items as JSON
    #         return cart_items
    #     return {}
    
    def clear(self):
        '''Clear the cart.'''
        self.cart = {}
        self.request.session['cart'] = self.cart
        self.save()