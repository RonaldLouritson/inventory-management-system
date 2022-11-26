from django.contrib import admin
from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views
from . import views

admin.site.site_title = 'KIRATECH'
admin.site.index_title = 'KIRATECH INVENTORY MANAGEMENT SYSTEM'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inventory', mainPage, name='mainPage'),
    path('inventory/<id>', get_Inventory_byid, name='get_Inventory_byid'),
    path('api/inventory', get_Inventorys, name='get_Inventorys'),


    #path('api/inventory/<id>', get_Inventorys_byid, name='get_Inventorys_byid'),
    #path('api/inventory', views.InventoryList.as_view(), name='inventory'),
]
