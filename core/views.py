import stripe
import requests
import uuid
from django.conf import settings
from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from core.forms import CheckoutForm, CouponForm
from core.models import Item, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def works(request):
    return  render(request, 'carousels.html')

def catalog(request):
    if not request.user.is_authenticated:
        try:
            print(request.session['nonuser'])
        except:
            request.session['nonuser'] = str(uuid.uuid4())
            print('dfgdfgdfgdfg')
            print(request.session['nonuser'])
            request.session.save()
    products = Item.objects.filter(category__title="Каталог")
    products1 = Item.objects.filter(category__title="Саженцы")
    products2 = Item.objects.filter(category__title="Сеянцы")

    context = {
        'object_list': products,
        'object_list1': products1,
        'object_list2': products2,
    }
    return  render(request, 'catalog.html', context)

def order_summary(request):
    order = Order.objects.get_or_create(session_id=request.session['nonuser'])
    context = {
        'objects': order
    }
    return render(request, 'order-summary.html', context)


def home(request):
    if not request.user.is_authenticated:
        try:
            print(request.session['nonuser'])
        except:
            request.session['nonuser'] = str(uuid.uuid4())
            print('dfgdfgdfgdfg')
            print(request.session['nonuser'])
            request.session.save()
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


def add_to_cart(request, slug):
    print(slug)
    item = Item.objects.filter(slug=slug)[0]
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        session_id=request.session['nonuser'],
        ordered=False
    )
    order_qs = Order.objects.get_or_create(session_id=request.session['nonuser'], payment=False)
    if len(order_qs):
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(session_id=request.session['nonuser'], ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("/order-summary")


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.filter(user=self.request.user, payment=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("core:checkout")
    def post(self,*args, **kwargs):
        return redirect("/")

def clear_cart(request):
    order = Order.objects.filter(session_id=request.session['nonuser'],payment=False)[0]
    # print(order.items.get_queryset)
    for order_item in order.items.get_queryset():
        order.items.remove(order_item)
        order_item.delete()
    order.save()
    return redirect("core:order-summary")

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        session_id=request.session['nonuser'],
        payment=False,
    )

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                session_id=request.session['nonuser'],
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect("core:order-summary")
        else:
            return redirect("core:order-summary")
    else:
        return redirect("core:order-summary")


def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        session_id=request.session['nonuser'],
        payment=False,
    )

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                session_id=request.session['nonuser'],
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            return redirect("core:order-summary")
        else:
            return redirect("core:order-summary")
    else:
        return redirect("core:order-summary")