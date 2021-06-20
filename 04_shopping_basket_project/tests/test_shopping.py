import unittest
from main_codes.shopping_basket import ShoppingBasket
from parameterized import parameterized


class TestShoppingBasketWithNoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket without any product...')
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)

    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0)


class TestShoppingBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with one product...')
        cls.basket = ShoppingBasket().add_product('milk', 3.0)

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)

    def test_total_amount_should_have_tax(self):
        self.assertAlmostEqual(self.basket.total(), 3.0 * 1.21)

    def test_getting_product(self):
        p = self.basket.get_product(0)
        self.assertEqual(p.__repr__(), "Product(name='milk', price=3.0, quantity=1)")

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(1)


class TestShoppingBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n[INFO] Setting up basket with two products...')
        cls.basket = ShoppingBasket() \
            .add_product('milk', 3.0) \
            .add_product('water', 2.0)

    def test_size_of_basket_should_be_two(self):
        self.assertEqual(len(self.basket), 2)

    @parameterized.expand([
        (0, 'milk'),
        (1, 'water')
    ])
    def test_order_of_products(self, index, result):
        self.assertEqual(self.basket.get_product(index).name, result)

    def test_total_amount_should_have_tax(self):
        self.assertAlmostEqual(self.basket.total(), 5.0 * 1.21)

    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(2)
