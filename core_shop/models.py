# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import CartItem


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, help_text='Уникальное значение для URL категории')
    description = models.TextField(max_length = 2000)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core_shop:product_list_by_category', args=[self.slug])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.BooleanField(default=False)
    cart = models.ForeignKey(CartItem, related_name='Корзина', verbose_name="Корзина", null=True)
    def __str__(self):
        return "Продавец" if self.customer else "Покупатель"

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Категория', verbose_name="Категория")
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    brand = models.CharField(max_length = 50, verbose_name="Производитель")
    image = models.ImageField(upload_to='product/pictures', default = 'product/no-img.png', verbose_name='Изображение')
    slug = models.SlugField(max_length=255, unique=True, help_text='Уникальное значение для ULR продукта')
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    count = models.PositiveIntegerField(verbose_name="Количество на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, null=True,  related_name='Профиль')

    class Meta:
        db_table = 'products'
        ordering = ['name']
        index_together = [['id', 'slug']]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core_shop:product_detail', args=[self.id, self.slug])

