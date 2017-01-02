from django.conf.urls import url, include

urlpatterns = [ url('darknet_shop.cart.views',
                       (r'^$', 'show_cart', {'template_name': 'cart/detail.html'}, 'show_cart')), ]
