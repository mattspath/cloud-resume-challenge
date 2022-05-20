import unittest
from index import dynamodb, table, ddbTableName

class TestDDB(unittest.TestCase):
    def test_dynamodb(self):
        self.assertIsNotNone(dynamodb)

    def test_table(self):
        self.assertIsNotNone(table)
        self.assertEqual(ddbTableName, 'SiteCounter')

if __name__ == '__main__':
    unittest.main()