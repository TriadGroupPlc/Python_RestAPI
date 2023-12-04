from unittest import TestCase

import readAllCustomers

file = 'test_resources/Customers_Test.json'


class Test(TestCase):
    def test_read_all_customer(self):
        customer_data = readAllCustomers.read_all_customer(file)
        if customer_data:
            self.assertTrue(customer_data is not None)
            self.assertEqual(len(customer_data), 3)
