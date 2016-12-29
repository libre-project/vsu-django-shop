from django import forms
from .models import Category, Product
import django_filters

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'brand', 'category','image', 'price', 'description', 'available', 'count',  )

class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label = 'Название содержит')
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt', label = 'Цена более')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt', label = 'Цена менее')
    class Meta:
        model = Product
        fields = ( 'category',  )
<<<<<<< HEAD
=======
        # fields = {
        #         'price': ['lt', 'gt'],
        # }

class ProductBuyForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()

>>>>>>> 915e4778a6389bab66825eb4f3ae45470fd588e0
