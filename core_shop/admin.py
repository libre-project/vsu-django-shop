from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ('name',)
    ordering = ['name']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'count', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'count', 'available']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)
