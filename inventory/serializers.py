from .models import *
from rest_framework import serializers

class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    class Meta:
        model = Inventory
        fields = ('__all__')


class InventorySelectedFieldsSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField()
    class Meta:
        model = Inventory
        fields = ('id', 'name','availability','supplier')


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ('__all__')