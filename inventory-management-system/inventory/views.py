from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InventorySerializer
from .models import Inventory, Supplier

# index page
def get_inventory(request):
    return render(request, 'inventory/index.html')


# API enpoint
@api_view(['GET'])
def get_APIInventorys(request):

    name = request.GET.get('name')

    if name:
        inventory = Inventory.objects.filter(name__contains=name) #by name data
    else:        
        inventory = Inventory.objects.all() #all data

    serialized = InventorySerializer(inventory, many=True)

    return Response(serialized.data)

def get_inventory_byID(request, id):
    try:
        inventory = Inventory.objects.get(id=id)
        context = {'inventory': inventory}
    except:
        context = {}
    return render(request, 'inventory/item_details.html', context)