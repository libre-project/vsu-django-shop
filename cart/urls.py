from django.conf.urls import *
from . import views


urlpatterns = [
    url(r'^$', views.show_cart, {'template_name': 'cart/detail.html'}, name='show_cart'),
]