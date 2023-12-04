from unittest import TestCase

import saveCustomer, os

file = '../test_resources/Customers_Test.json'
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, file)


class Test(TestCase):
    def test_save_existing_customer(self):
        customer = {
            'Title': 'Mr',
            'Name': 'Dave',
            'Address': '1st street Lincoln',
            'Phone': '1234579898',
            'Reference': 2
        }
        self.assertEqual('customer already exists', saveCustomer.save_customer(customer, path))

    def test_save_new_customer(self):
        customer = {
            'Title': 'Mr',
            'Name': 'Dave',
            'Address': '1st street Lincoln',
            'Phone': '1234579898',
            'Reference': 9
        }
        self.assertEqual('customer added successfully', saveCustomer.save_customer(customer, path))
