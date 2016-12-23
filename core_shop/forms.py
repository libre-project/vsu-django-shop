from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'brand', 'category', 'price', 'description', 'available', 'count',  )
