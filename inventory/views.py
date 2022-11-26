from django.shortcuts import get_object_or_404, render
import sweetify
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework.views import APIView

import requests


## web application
@login_required()
def mainPage(request):

    field = Inventory._meta.fields

    startwith = request.GET.get('Sstartwith')
    variable_column = request.GET.get('Sfilterby')
    
    if (startwith != None and variable_column != None) and (startwith != '' and variable_column != ''):
        search_type = 'contains'
        filter = variable_column + '__' + search_type

        url = 'http://localhost:8080/api/inventory?Sfilterby=' + variable_column + '&Sstartwith=' + startwith
        responses = requests.get(url).json

        if variable_column == 'availability':
            record = Inventory.objects.select_related().filter(availability=startwith).values('id','name','description','note','stock','availability','supplier__name').order_by('name')
        elif variable_column == 'supplier':
            getSupId = Supplier.objects.filter(name=startwith).values('id')
            if getSupId:
                record = Inventory.objects.select_related().filter(supplier=getSupId[0]['id']).values('id','name','description','note','stock','availability','supplier__name')
        else:
            record = Inventory.objects.select_related().filter(**{ filter: startwith }).values('id','name','description','note','stock','availability','supplier__name').order_by('name')
        

    else:
        record = Inventory.objects.all().order_by('name')
        responses = requests.get('http://localhost:8080/api/inventory').json


    context = {
        'fieldS': field,
        'recordS': record,
        'responseS': responses,
    }

    return render(request,"inventory/index.html",context)


## Get All inventory or filter by Name
@api_view(['GET'])
#@permission_classes(AllowAny)
def get_Inventorys(request):
    startwith = request.GET.get('Sstartwith')
    variable_column = request.GET.get('Sfilterby')

    if (startwith != None and variable_column != None) and (startwith != '' and variable_column != ''):
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        if variable_column == 'availability':
            inventorys = Inventory.objects.select_related().filter(availability=startwith).values('id','name','description','note','stock','availability','supplier__name').order_by('name')
        elif variable_column == 'supplier':
            getSupId = Supplier.objects.filter(name=startwith).values('id')
            if getSupId:
                inventorys = Inventory.objects.select_related().filter(supplier=getSupId[0]['id'])
        else:
            inventorys = Inventory.objects.select_related().filter(**{ filter: startwith }).values('id','name','description','note','stock','availability','supplier__name').order_by('name')

    else:
        inventorys = Inventory.objects.all()
    
    if inventorys:
        serialized = InventorySerializer(inventorys, context={'request': request}, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


    return Response({'No Record Found!'}, status=status.HTTP_400_BAD_REQUEST)


## Get inventory imtem by ID
def get_Inventory_byid(request, id):
    field = Inventory._meta.fields
    if id is not None and id != '':
        if id.isdigit():
            record = Inventory.objects.filter(id=id).order_by('name')

    context = {
        'fieldS': field,
        'recordS': record,
    }

    return render(request,"inventory/itemdetails.html",context)
            


## Get inventory imtem by ID for API
@api_view(['GET'])
#@permission_classes(AllowAny)
def get_Inventorys_byid(request, id):
    if id is not None and id != '':
        if id.isdigit():
            inventory = get_object_or_404(Inventory, id=id)
            if inventory:
                serialized = InventorySerializer(inventory, context={'request': request})
                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response({'No Record Found!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Not a Valid Item Id!'}, status=status.HTTP_400_BAD_REQUEST)  

    return Response({'Not a Valid Item Id!'}, status=status.HTTP_400_BAD_REQUEST)




###class base view
class InventoryList(generics.ListAPIView):
    serializer_class = InventorySelectedFieldsSerializer

    def get_queryset(self):
        queryset = Inventory.objects.all().values('name','supplier','availability')
        name = self.request.query_params.get('name')
        if name is not None and name != '':
            queryset = queryset.filter(name=name)
        return queryset