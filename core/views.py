import stripe
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from core.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    products = Item.objects.all()
    context = {
        'object_list': products,
    }
    return render(request, 'home.html', context)


def detail(request, slug):
    item = Item.objects.filter(slug=slug)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)