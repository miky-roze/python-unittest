import unittest
from unittest.mock import patch
from code_project.code_generator import get_code, get_code_with_day


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_get_code_mock_3(self, mocked_randint):
        mocked_randint.return_value = 3
        self.assertEqual(get_code(), 'XC-3')

    @patch('random.randint')
    def test_get_code_mock_5(self, mocked_randint):
        mocked_randint.return_value = 5
        self.assertEqual(get_code(), 'XC-5')

    @patch('random.randint')
    def test_get_code_mock_9(self, mocked_randint):
        mocked_randint.return_value = 9
        self.assertEqual(get_code(), 'XC-9')


class TestGetCodeWithDay(unittest.TestCase):

    @patch('code_project.code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_1_with_monday(self, mocked_randint, mocked_today):
        mocked_randint.return_value = 1
        mocked_today.return_value = 'Mon'

        self.assertEqual(get_code_with_day(), 'XC-1-MON')

    @patch('code_project.code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_4_with_wednesday(self, mocked_randint, mocked_today):
        mocked_randint.return_value = 4
        mocked_today.return_value = 'Wed'

        self.assertEqual(get_code_with_day(), 'XC-4-WED')

    @patch('code_project.code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_7_with_friday(self, mocked_randint, mocked_today):
        mocked_randint.return_value = 7
        mocked_today.return_value = 'Fri'

        self.assertEqual(get_code_with_day(), 'XC-7-FRI')
