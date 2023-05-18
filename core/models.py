from django.core.checks import messages
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.http import request
from django.shortcuts import reverse, get_object_or_404, redirect
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    image = models.ImageField(default=None)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    title = models.CharField(max_length=100)
    height = models.CharField(max_length=100, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    slug = models.SlugField()
    description = models.TextField(default="NONE")
    image = models.ImageField()
    def __str__(self):
        return self.title

    def get_price(self):
        return int(self.price)

    def get_absolute_url(self):
        return reverse("core:detail", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    session_id = models.CharField(max_length=100, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return int(self.quantity * self.item.price)

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        return self.get_total_item_price()


class Order(models.Model):
    session_id = models.CharField(max_length=100, null=True)
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(OrderItem)
    payment=models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True)
    def __str__(self):
        return "Номер заказа: " + str(self.id)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return int(total)
