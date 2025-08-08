import unittest
from src.database import DatabaseConnection, QueryBuilder
from src.models import Customer, Payment, Shipping

class TestDatabase(unittest.TestCase):
    def test_database_connection(self):
        db = DatabaseConnection("localhost", 5432, "test_db")
        self.assertTrue(db.connect())
        self.assertTrue(db.connected)
    
    def test_query_builder(self):
        query = QueryBuilder().select(["id", "name"]).from_table("users").where("id = 1")
        expected = "SELECT id, name FROM users WHERE id = 1"
        self.assertEqual(query.build(), expected)
    
    def test_customer_creation(self):
        customer = Customer("cust_123", "John Doe", "john@example.com", "123-456-7890")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
    
    def test_payment_processing(self):
        payment = Payment("pay_456", 100.0, "credit_card", "pending")
        self.assertTrue(payment.process())
        self.assertEqual(payment.status, "completed")
    
    def test_shipping_creation(self):
        shipping = Shipping("ship_789", "123 Main St", "express")
        self.assertEqual(shipping.status, "pending")
        self.assertTrue(shipping.ship())
        self.assertEqual(shipping.status, "shipped")

if __name__ == '__main__':
    unittest.main()
