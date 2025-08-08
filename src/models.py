class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def to_dict(self):
        return {'name': self.name, 'email': self.email}

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def get_price_with_tax(self, tax_rate=0.1):
        return self.price * (1 + tax_rate)

class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products
        self.created_at = time.time()
    
    def get_total(self):
        return sum(product.get_price_with_tax() for product in self.products)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'products': [product.to_dict() for product in self.products],
            'total': self.get_total(),
            'created_at': self.created_at
        }

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, product, quantity):
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {
                'product': product,
                'quantity': quantity
            }
    
    def get_available_quantity(self, product_id):
        return self.items.get(product_id, {}).get('quantity', 0)
