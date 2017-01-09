from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        # remove products from stock
        count = cd['quantity']
        # if product count is invalid
        if count > product.count:
            # buy all products
            cart.add(product=product, quantity=product.count,
                     update_quantity=cd['update'])
            product.change_count(-product.count)
        else:
            cart.add(product=product, quantity=cd['quantity'],
                     update_quantity=cd['update'])
            product.change_count(-cd['quantity'])
    return redirect('cart:CartDetail')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

def CartDetail(request):
    if not request.user.is_authenticated:
        return redirect('/')
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'cart/detail.html',
                 {'cart': cart})

