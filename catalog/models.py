from django.db import models

#Модель категории
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length = 50, unique = True, help_text='Уникальное значение для URL продукта')
    description = models.TextField(max_length = 2000)
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField("Meta Keywords", max_length = 255, help_text = 'Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length = 255, help_text = 'Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('catalog_category', args = (self.slug))

#Модель продукта
class Product(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(max_length = 255, unique = True)
    brand = models.CharField(max_length = 50)
    sku = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    old_price = models.DecimalField(max_digits = 9, decimal_places = 2, blank = True, default = 0.00)
    image = models.CharField(max_length = 50)
    is_active = models.BooleanField(default = False)
    is_bestseller = models.BooleanField(default = False)
    is_featured = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length = 255)
    meta_description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args = (self.slug))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
