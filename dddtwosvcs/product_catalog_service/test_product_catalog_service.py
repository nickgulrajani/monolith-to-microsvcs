import unittest
from unittest.mock import patch
from product_catalog_service import app

class TestProductCatalogService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('product_catalog_service.get_products_from_database')
    def test_get_products(self, mock_get_products_from_database):
        mock_get_products_from_database.return_value = [
            {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10.0, 'vendor': 'Vendor 1'},
            {'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 20.0, 'vendor': 'Vendor 2'},
            {'id': 3, 'name': 'Product 3', 'description': 'Description 3', 'price': 30.0, 'vendor': 'Vendor 3'}
        ]
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        expected_response = [
            {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10.0, 'vendor': 'Vendor 1'},
            {'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 20.0, 'vendor': 'Vendor 2'},
            {'id': 3, 'name': 'Product 3', 'description': 'Description 3', 'price': 30.0, 'vendor': 'Vendor 3'}
        ]
        self.assertEqual(response.get_json(), expected_response)

if __name__ == '__main__':
    unittest.main()

