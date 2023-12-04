from unittest import TestCase

import validateCustomer

file = 'test_resources/Customers_Test.json'


class Test(TestCase):

    def test_validate_customer_present(self):
        self.assertTrue(validateCustomer.find_ref_customer(2, file))

    def test_validate_customer_absent(self):
        self.assertFalse(validateCustomer.find_ref_customer(10, file))