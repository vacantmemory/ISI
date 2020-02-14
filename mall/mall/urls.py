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
from mall.view import *
from mall.product import product_list, filter_product
urlpatterns = [
    path(r'admin/', admin.site.urls),

    url(r'^hello/$', greeting),

    # account
    url(r'^home/$', home, name='home_link'),
    url(r'^login/$', login),
    url(r'^user_login/$', loginCheck),
    url(r'^user_sign_up/$', registerSystem),
    url(r'^register/$', register, name='register_link'),

    # product
    url(r'^product/([0-9]?)/$', product_list),
    url(r'^Search/$', filter_product),

    # order
    url(r'^orders/$', orderListing),
    url(r'^order_detail/([A-Za-z0-9]+)/$', orderDetail, name='order_detail_link'),

    # order for vendor
    url(r'^ship_order/([A-Za-z0-9]+)/$', shipOrder, name='ship_order_link'),
    url(r'^search_order/$', searchOrder, name='search_order_link'),

    # test url
    url(r'^test/$', test),

]
