from .models import Inventory
from rest_framework import serializers

class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.ReadOnlyField(source='supplier.name')  # Return the supplier name instead of id
    class Meta:
        model = Inventory
        fields = ('id', 'name','availability','supplier')