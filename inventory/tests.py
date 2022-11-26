from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from rest_framework import status
from django.test import SimpleTestCase
from .views import get_Inventorys


class InventoryTestCase(APITestCase):
    def test_inventory(self):
        response=self.client.get(reverse('get_Inventorys'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data)


    def test_inventory_byid(self):
        url = reverse("get_Inventory_byid", kwargs={"id": 1})
        response = self.client.get(url)
        # response=self.client.get(reverse('get_Inventory_byid'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data)


    def test_mainPage(self):
        response=self.client.get(reverse('mainPage'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data)



        #url = reverse('get_Inventorys')
        #print(url)
        #print(resolve(url).func)
        #self.assertEqual(resolve(url).func.view, get_Inventorys)

        # response=self.client.get(reverse('get_Inventorys'))

        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data)