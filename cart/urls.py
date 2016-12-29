from django.cpnf.urls.defaults import *

urlpatterns = patterns('darknet_shop.cart.views',
                       (r'^$', 'show_cart', {'template_name': 'cart/detail.html'}, 'show_cart'),
                       )