from django.test import TestCase
from django.test import Client

# Create your tests here.


class InventoryTestCase(TestCase):
    def setUp(self):
        # Create the client
        self.client = Client()

    def test_get_APIInventorys(self):
        # Visit the inventory list page
        response = self.client.get('/api/inventory', follow=True)

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)

    def test_get_inventory(self):
        # Visit the inventory list page
        response = self.client.get('/inventory')

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)

    def test_get_inventory_byID(self):
        # Visit the inventory list page
        response = self.client.get('/inventory/1')

        # Assert whether the response is equal to 200 or not
        self.assertEqual(response.status_code, 200)