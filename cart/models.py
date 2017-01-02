from __future__ import unicode_literals
from django.db import models


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    product = models.ForeignKey('core_shop.Product', unique=False, related_name='product_item')

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.count*self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def argument_count(self, count):
        self.count += int(count)
        self.save()


class Order(models.Model):
    profile = models.ForeignKey('core_shop.Profile', blank=True, null=True, related_name = 'owner')
    date_added = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('core_shop.Product', through='ProductInOrder')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey('core_shop.Product')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()

