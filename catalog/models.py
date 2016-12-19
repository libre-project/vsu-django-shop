from django.db import models

#Модель категории
class category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length = 50, unique = True, help_text='Уникальное значение для URL продукта')
    description = models.TextField(max_length = 2000)
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField("Meta Keywords", max_length = 255. help_text = 'Comma-delimited set of SEO keywords for meta tag')
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
