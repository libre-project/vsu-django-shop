from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', views.product_edit, name='product_edit'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail')
]
