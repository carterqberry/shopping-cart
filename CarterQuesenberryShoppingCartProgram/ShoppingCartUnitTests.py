#carter quesenberry unit tests

import unittest
from ShoppingCart import Product
from ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    # unit tests from test_shopping_cart-1.py:
    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = Product("Apple", 1.0, 5)
        self.product2 = Product("Banana", 0.5, 10)

    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Apple")
        print("test_add_product: Passed")

    def test_remove_product(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.remove_product("Apple")
        self.assertTrue(len(self.cart.products) == 1)
        self.assertEqual(self.cart.products[0].name, "Banana")
        print("test_remove_product: Passed")

    def test_update_quantity(self):
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Apple", 10)
        self.assertEqual(self.cart.products[0].quantity, 10)
        print("test_update_quantity: Passed")

    def test_calculate_subtotal(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(self.cart.calculate_subtotal(), 10.0)
        print("test_calculate_subtotal: Passed")

    def test_set_tax_rate(self):
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.tax_rate, 0.08)
        print("test_set_tax_rate: Passed")

    def test_calculate_tax(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_tax(), 0.8)
        print("test_calculate_tax: Passed")

    def test_calculate_total(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.cart.set_tax_rate(0.08)
        self.assertEqual(self.cart.calculate_total(), 10.8)
        print("test_calculate_total: Passed")

    # requirement 4:
    # new unit tests:
    def test_remove_nonexistent_product(self):
        self.cart.add_product(self.product1)
        self.cart.remove_product("Orange")  # trying to remove a product that is not in the cart
        self.assertEqual(len(self.cart.products), 1)  # the cart should not change
        print("test_remove_nonexistent_product: Passed")

    def test_update_nonexistent_product_quantity(self):
        self.cart.add_product(self.product1)
        self.cart.update_quantity("Orange", 10)  # trying to update the quantity of a product that doesnt exist
        self.assertEqual(self.cart.products[0].quantity, 5)  # the quantity should not change
        print("test_update_nonexistent_product_quantity: Passed")

    def test_calculate_subtotal_with_zero_quantity(self):
        zero_quantity_product = Product("Zero", 2.0, 0)
        self.cart.add_product(zero_quantity_product)
        self.assertEqual(self.cart.calculate_subtotal(), 0.0)  # the subtotal should not include this product
        print("test_calculate_subtotal_with_zero_quantity: Passed")

    def test_set_negative_tax_rate(self):
        with self.assertRaises(ValueError):
            self.cart.set_tax_rate(-0.08)  # trying to set a negative tax rate should raise ValueError
        print("test_set_negative_tax_rate: Passed")

if __name__ == "__main__":
    unittest.main()
