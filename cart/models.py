from __future__ import unicode_literals
from django.db import models
from core_shop.models import Product
from core_shop.models import Profile


class Order(models.Model):
    profile = models.ForeignKey(Profile, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='ProductInOrder')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()

