import unittest
from unittest.mock import patch
from code_project.tech_stack import TechStack


class TestTechStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = TechStack()
        self.stack.add_tech('python') \
            .add_tech('java') \
            .add_tech('sql') \
            .add_tech('aws') \
            .add_tech('c++')

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_sql(self, mocked_get_tech):
        mocked_get_tech.return_value = 'sql'
        self.assertEqual(self.stack.get_tech(), 'sql')

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_python(self, mocked_get_tech):
        mocked_get_tech.return_value = 'python'
        self.assertEqual(self.stack.get_tech(), 'python')
