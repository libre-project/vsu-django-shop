from django import forms
from .models import Category, Product
import django_filters

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'brand', 'category', 'price', 'description', 'available', 'count',  )

class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ( 'price', 'category',  )

