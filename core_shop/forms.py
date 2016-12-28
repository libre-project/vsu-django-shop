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
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')
    class Meta:
        model = Product
        fields = ( 'category',  )
        # fields = {
        #         'price': ['lt', 'gt'],
        # }

class ProductBuyForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()

