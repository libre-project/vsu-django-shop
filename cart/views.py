from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404


def shopping_cart(request, template_name='orders/shopping_cart.html'):
    cart = get_shopping_cart(request)
    ctx = {'cart': cart}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


def add_to_cart(request, queryset, id=None, slug=None, slug_field='slug', template_name='orders/add_to_cart.html'):
    product = lookup_object(queryset, id, slug, slug_field)
    count = request.GET.get('count', 1)
    cart = get_shopping_cart(request)
    cart.add_item(product, count)
    update_shopping_cart(request, cart)
    ctx = {'product': product, 'cart': cart}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


def remove_from_cart(request, queryset, id=None, template_name='orders/remove_from_cart.html'):
    cart = get_shopping_cart(request)
    cart.remove_item(id)
    update_shopping_cart(request, cart)
    ctx = {'cart': cart}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


def lookup_object(queryset, id=None, slug=None, slug_field=None):
    if id is not None:
        obj = queryset.get(pk=id)
    elif slug and slug_field:
        kwargs = {slug_field: slug}
        obj = queryset.get(**kwargs)
    else:
        raise Http404
    return obj


