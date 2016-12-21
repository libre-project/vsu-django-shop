# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Уникальное значение для URL категории')
    description = models.TextField(max_length = 2000)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # __unicode__ on Python 2 (чтобы в панели админа отображалось нормально)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core_shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    brand = models.CharField(max_length = 50, verbose_name="Производитель")
    slug = models.SlugField(max_length=255, unique=True, help_text='Уникальное значение для ULR продукта')
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    count = models.PositiveIntegerField(verbose_name="Количество на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['name']
        index_together = [['id', 'slug']]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core_shop:product_detail', args=[self.id, self.slug])
