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
from mall.product import product_list, upload, filter_product
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^hello/$', greeting),
    url('^login/$', login),
    url('^user_login/$', loginCheck),
    url('^product/$', product_list),
    url('^finish/$', filter_product),
    url('^product/1/$', filter_product)
]
