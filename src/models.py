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