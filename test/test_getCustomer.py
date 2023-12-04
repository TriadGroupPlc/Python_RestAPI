from unittest import TestCase

import getCustomer

file = 'test_resources/Customers_Test.json'


class Test(TestCase):
    def test_get_customer(self):
        self.assertFalse(getCustomer.get_customer(2, file).empty)
        self.assertTrue(getCustomer.get_customer(9, file).empty)