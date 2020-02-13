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
    path('admin/', admin.site.urls),
<<<<<<< HEAD

    url('^hello/$', greeting),

    #account
    url(r'^home/$', home, name='home_link'),
    url('^login/$', login),
    url('^user_login/$', loginCheck),
    url(r'^user_sign_up/$', registerSystem),
    url(r'^register/$', register, name='register_link'),

    # product
    url('^product/$', product_list),
    url('^Search/$', filter_product),

=======
    url(r'^hello/$', greeting),
    url(r'^login/$', login),
    url(r'^user_login/$', loginCheck),
    url(r'^product/$', product_list),
    url(r'^finish/$', filter_product),
    url(r'^product/1/$', filter_product),
    url(r'^register/$', register, name='register_link'),
    url(r'^user_sign_up/$', registerSystem),
    url(r'^home/$', home, name='home_link'),
    url(r'^orders/$', orderListing),
    url(r'^order_detail/([A-Za-z0-9]+)/$', orderDetail, name='order_detail_link'),

    # test url
    url(r'^test/$', test),
>>>>>>> 21ecb259c46925ce7e53e6b9474713acb571c34f
]
