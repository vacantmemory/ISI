"""mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView

from mall.view import *
from mall.product import *
from mall.cart import *

urlpatterns = [
    path(r'admin/', admin.site.urls),

    url(r'^hello/$', greeting),
    url(r'^$', RedirectView.as_view(url='login')),

    # account
    url(r'^home/$', home, name='home_link'),
    url(r'^login/$', login, name='login_link'),
    url(r'^user_login/$', loginCheck),
    url(r'^user_sign_up/$', registerSystem),
    url(r'^register/$', register, name='register_link'),
    url(r'^sign_out/$', signOut, name='sign_out_link'),

    # product
    url(r'^product/$', product_list, name='product_link'),
    url(r'^product/ascending/$', product_list),
    url(r'^product/descending/$', product_list),
    url(r'^product/search/$', product_list),
    url(r'^product/search_vendor/$', product_list),
    url(r'productDetail/(?P<pid>[0-9]+)/$', product_detail, name="detail_link"),

    # order
    url(r'^orders/$', orderListing, name='orders_link'),
    url(r'^order_detail/([A-Za-z0-9]+)/$', orderDetail, name='order_detail_link'),

    # order for vendor
    url(r'^ship_order/([A-Za-z0-9]+)/$', shipOrder, name='ship_order_link'),
    url(r'^search_order/$', searchOrder, name='search_order_link'),

    # cart
    url(r'^cart/$', cartListing, name='cart_link'),
    url(r'^add_to_cart/(?P<pid>[0-9]+)/$', addToCart, name='add_to_cart_link'),
    url(r'^remove_item_in_cart/(?P<pid>[0-9]+)/$', removeItem, name='remove_link'),
    url(r'^checkout/$', checkOut, name='checkout_link'),
    url(r'^cart_update/(?P<pid>[0-9]+)/$', updateQuantity, name='update_quantity_link'),

    # test url
    url(r'^test/$', test),
]
