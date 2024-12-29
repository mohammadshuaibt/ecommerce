from django.conf import settings

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url}
        self.save()

    def remove(self, product_id):
        """Remove a product from the cart."""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self,product_id,quantity):
        '''Update the quantity of a product in Cart.'''
        product_id = str(product_id)
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.remove(product_id)
            self.save()

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