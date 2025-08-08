from src.database import DatabaseConnection, QueryBuilder
from src.models import Customer, Payment, Shipping

class App:
    def __init__(self):
        self.name = 'Outdated Test App 2 - UPDATED'
        self.version = '3.0.0'
        self.features = ['basic', 'advanced', 'database']
        self.db = None
    
    def run(self):
        print(f'Running {self.name} v{self.version}')
        self.new_feature()
        self.setup_database()
        return True
    
    def get_info(self):
        return {
            'name': self.name,
            'version': self.version,
            'features': self.features
        }
    
    def new_feature(self):
        print('New feature added to simulate outdated state')
        return 'feature_added'
    
    def process_data(self, data):
        # New method to process data
        return [item * 2 for item in data]
    
    def setup_database(self):
        # Setup database connection
        self.db = DatabaseConnection("localhost", 5432, "test_db")
        return self.db.connect()
    
    def create_customer(self, name: str, email: str, phone: str) -> Customer:
        # Create a new customer
        customer = Customer("cust_123", name, email, phone)
        return customer
    
    def process_payment(self, amount: float, method: str) -> Payment:
        # Process a payment
        payment = Payment("pay_456", amount, method, "pending")
        payment.process()
        return payment
    
    def create_shipping(self, address: str, method: str) -> Shipping:
        # Create shipping
        shipping = Shipping("ship_789", address, method)
        return shipping

def main():
    app = App()
    return app.run()

if __name__ == '__main__':
    main()
