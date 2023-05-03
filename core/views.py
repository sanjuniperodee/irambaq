import stripe
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from core.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    products = Item.objects.filter(category__title="Каталог")
    products1 = Item.objects.filter(category__title="Саженцы")
    products2 = Item.objects.filter(category__title="Сеянцы")

    context = {
        'object_list': products,
        'object_list1': products1,
        'object_list2': products2,
    }
    return render(request, 'home.html', context)


def detail(request, slug):
    item = Item.objects.filter(slug=slug)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)