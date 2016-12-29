from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^filter/$', views.product_list_f, name = 'product_filter'),
    url(r'^login/$', auth_view.login, { 'template_name' : 'shop/login.html'}, name='login'),
    url(r'^logout/$', auth_view.logout, { 'next_page' : '/'  }, name='logout'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', views.product_edit, name='product_edit'),
    url(r'^product/(?P<id>\d+)/(?P<slug>[-\w]+)/delete/$', views.product_delete, name='product_delete'),
    url(r'^product/(?P<id>\d+)/(?P<slug>[-\w]+)/buy/$', views.product_buy, name='product_buy'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail')

]

