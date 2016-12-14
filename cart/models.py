from __future__ import unicode_literals
from django.db import models
from core_shop.models import Product


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    product = models.ForeignKey('core_shop.Product', unique=False)

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
