from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    category = product.category.name
    page_title = product.name
    return render(request, 'shop/product/detail.html', {'product': product})

def is_customer(request):
    if request.Profile.user.is_authenticated():
        current_user = request.Profile
        if current_user.customer:
            return True
        else:
            return False
    else:
        return False
