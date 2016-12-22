from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Product, Profile


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

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'

class UserAdmin(UserAdmin):
    inlines = (ProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
