import unittest
from sqlite3 import connect
from main_codes.customersDB import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        # Arrange
        db = CustomersDB(self.connection)
        cursor = self.connection.cursor()

        # Act
        lastRowId = db.add_customer('Mike', 'Jordan', 'mike.jordan@mail.com', '444', 'PL')
        cursor.execute("""SELECT * FROM customers WHERE last_name='Jordan'""")

        # Assert
        self.assertEqual(lastRowId, 4)
        self.assertEqual(next(cursor), ('Mike', 'Jordan', 'mike.jordan@mail.com', '444', 'PL'))

    def test_find_customers_by_first_name(self):
        # Arrange
        db = CustomersDB(self.connection)

        # Act
        customersNamedJohn = tuple(db.find_customers_by_first_name('John'))

        # Assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
        self.assertEqual(customersNamedJohn, expected)

    def test_find_customers_by_country(self):
        # Arrange
        db = CustomersDB(self.connection)

        # Act
        customersFromUSA = tuple(db.find_customers_by_country('USA'))

        # Assert
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(customersFromUSA, expected)
