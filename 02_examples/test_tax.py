import unittest
from tax import calc_tax

# Tests are focused on age parameter


class TestCalcTax(unittest.TestCase):
    def test_age_incorrect_type_raises_error(self):
        with self.assertRaises(TypeError):
            calc_tax(100, 0.23, 18.0)
            calc_tax(100, 0.23, '18')

    def test_age_incorrect_value_raises_error(self):
        with self.assertRaises(ValueError):
            calc_tax(100, 0.23, 0)
            calc_tax(100, 0.23, -1)

    def test_tax_amount_age_18_tax_less_than_5000(self):
        self.assertEqual(calc_tax(100, 0.23, 18), 23, "Wrong result for tax payer age 18, tax 23")

    def test_tax_amount_age_18_tax_greater_than_5000(self):
        self.assertEqual(calc_tax(100000, 0.23, 18), 5000, "Wrong result for tax payer age 18, tax 23000")

    def test_tax_amount_age_56(self):
        self.assertAlmostEqual(calc_tax(100, 0.23, 56), 23, 7, "Wrong result for tax payer age 56, tax 23")

    def test_tax_amount_age_70_tax_less_than_8000(self):
        self.assertEqual(calc_tax(100, 0.23, 70), 23, "Wrong result for tax payer age 18, tax 23")

    def test_tax_amount_age_70_tax_greater_than_8000(self):
        self.assertEqual(calc_tax(100000, 0.23, 70), 8000, "Wrong result for tax payer age 18, tax 23000")


if __name__ == '__main__':
    unittest.main()
