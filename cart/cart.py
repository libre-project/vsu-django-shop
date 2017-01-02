from django.conf import settings
from cart.models import CartItem
from core_shop.models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from decimal import Decimal
import uuid

CART_ID_SESSION_KEY = 'cart_id'


def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cart_id():
    return str(uuid.uuid4())


def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))


def add_to_cart(request, product, count):
    #postdata = request.POST.copy()
    # get product slug, return blank if empty
    #product_slug = postdata.get('product_slug', '')
    # get count added, return 1 if empty
    #count = postdata.get('count', 1)

    #product = get_object_or_404(Product, slug=product_slug)
    cart_products = get_cart_items(request)
    product_in_cart = False
    # if item is already in cart
    for item in cart_products:
        if item.product.id == product.id:
            item.argument_count(count)
            product_in_cart = True
    if not product_in_cart:
        cart_item = CartItem()
        cart_item.product = product
        cart_item.count = count
        cart_item.cart_id = _cart_id(request)
        cart_item.save()


def cart_distinct_item_count(request):
    return get_cart_items(request).count()

"""
class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновление количества товара
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Итерация по товарам
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
"""