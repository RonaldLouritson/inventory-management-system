from django.urls import path
from .views import get_inventory, get_APIInventorys, get_inventory_byID


urlpatterns = [
    path('inventory', get_inventory, name='get_inventory'),
    path('inventory/<id>', get_inventory_byID, name='get_inventory_byID'),
    path('api/inventory', get_APIInventorys, name='get_APIInventorys'),
]


