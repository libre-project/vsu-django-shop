import unidecode
from unidecode import unidecode
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm, ProductDeleteForm, ProductFilter
from cart.forms import CartAddProductForm
from django.utils import timezone
from django.utils.text import slugify

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category, 'categories': categories, 'products': products})

def product_list_f(request):
    f = ProductFilter(request.GET, queryset = Product.objects.all())
    return render(request, 'shop/product/filter.html', { 'filter' : f })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})


def is_customer(request):
    if request.Profile.user.is_authenticated():
        current_user = request.Profile
        if current_user.customer:
            return True
        else:
            return False
    else:
        return False

def product_new(request):
    if not request.user.profile.customer:
        return redirect('/')
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit = False)
            product.created_at = timezone.now()
            product.updated_at = timezone.now()
            product.slug = slugify(unidecode(product.name))
            product.profile = request.user.profile
            product.save()
            # return render(request, 'shop.views.product_detail',{'id': product.id, 'slug':product.slug})
            return redirect('/')
    else:
        form = ProductForm()
        return render(request, 'shop/product/product_edit.html', {'form' : form})

def product_edit(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug)
    if request.user != product.profile.user or not request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            product = form.save(commit = False)
            product.created_at = timezone.now()
            product.updated_at = timezone.now()
            product.slug = slugify(unidecode(product.name))
            product.save()
            # return redirect('shop.views.product_detail', id = product.id, slug = product.slug)
            # return render(request, 'shop.views.product_detail',{'id': product.id, 'slug':product.slug})
            return redirect('/')
    else:
        form = ProductForm(instance = product)
        return render(request, 'shop/product/product_edit.html', {'form' : form})

def product_delete(request, id, slug):
    product_to_delete = get_object_or_404(Product, id = id, slug = slug)
    if request.user != product_to_delete.profile.user or not request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = ProductDeleteForm(request.POST, instance = product_to_delete)
        if form.is_valid():
            product_to_delete.delete()
            return redirect('/')
    else:
        form = ProductDeleteForm(instance = product_to_delete)
    return render(request, 'shop/product/product_delete.html', {'form' : form, 'product' : product_to_delete})
