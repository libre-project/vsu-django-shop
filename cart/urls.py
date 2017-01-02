<<<<<<< HEAD
from django.conf.urls import url, include

urlpatterns = [ url('darknet_shop.cart.views',
                       (r'^$', 'show_cart', {'template_name': 'cart/detail.html'}, 'show_cart')), ]
=======
from django.conf.urls import *
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.show_cart, {'template_name': 'cart/detail.html'}, name='show_cart'),
]
>>>>>>> fbf9ce591155f986159f280984f8aa34bf96cf9a
