import time
from typing import Dict, Any, List

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

# New models added to further simulate outdated state
class Customer:
    def __init__(self, id: str, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at
        }

class Payment:
    def __init__(self, id: str, amount: float, method: str, status: str):
        self.id = id
        self.amount = amount
        self.method = method
        self.status = status
        self.processed_at = time.time()
    
    def process(self) -> bool:
        # Simulate payment processing
        self.status = "completed"
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'amount': self.amount,
            'method': self.method,
            'status': self.status,
            'processed_at': self.processed_at
        }

class Shipping:
    def __init__(self, id: str, address: str, method: str):
        self.id = id
        self.address = address
        self.method = method
        self.status = "pending"
    
    def ship(self) -> bool:
        # Simulate shipping
        self.status = "shipped"
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'address': self.address,
            'method': self.method,
            'status': self.status
        }
