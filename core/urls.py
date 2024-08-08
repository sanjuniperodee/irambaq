from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('nashi_raboty', works, name='nashi_raboty'),
    path('catalog', catalog, name='catalog'),
    path('detail<str:slug>', detail, name='detail'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('order-summary/', order_summary, name='order-summary'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('order-clear/', clear_cart, name='clear_cart'),
    # path('add-to-cart1', add_to_cart1, name='add-to-cart1'),
]