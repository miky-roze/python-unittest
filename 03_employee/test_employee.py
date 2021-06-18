import unittest
from employee import Employee

# TO TEST:
# 1. Is email address correct?
# 2. Will email address be correct after change of a first name
# 3. Will email address be correct after change of a last name
# 4. Is tax calculated correctly?
# 5. Does applying bonus work correctly?


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('John', 'Smith', 80000)

    def tearDown(self):
        del self.employee

    def test_correct_email_address(self):
        self.assertEqual(self.employee.email, 'john.smith@mail.com')

    def test_correct_email_address_after_first_name_change(self):
        self.employee.first_name = 'Mike'
        self.assertEqual(self.employee.email, 'mike.smith@mail.com')

    def test_correct_email_address_after_last_name_change(self):
        self.employee.last_name = 'Jordan'
        self.assertEqual(self.employee.email, 'john.jordan@mail.com')

    def test_correct_tax_calculation(self):
        self.assertAlmostEqual(self.employee.tax, 13600)

    def test_correct_bonus_application(self):
        self.employee.apply_bonus()
        self.assertEqual(self.employee.salary, 88000)


if __name__ == '__main__':
    unittest.main()
