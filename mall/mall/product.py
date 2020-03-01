from django.shortcuts import render
from ISI.models import product, properties, shopcartRecord
import decimal
from mall.account import identityCheck


def product_list(request):
    ascending = request.POST.get("Ascending")
    descending = request.POST.get("Descending")
    brand = request.POST.get("brand")
    data = request.POST.get("find")
    p_list = product.objects.all()
    msg = ''
    ss = ''
    # sort
    if ascending:
        p_list = ascending_product(p_list)
    if descending:
        p_list = descending_product(p_list)
    # search_c
    if brand:
        p_list = search_c(brand)
        ss = 'a'
        if not p_list:
            msg = "Not Found"
    # search_v
    if data:
        p_list = search_vendor(data)
        if not p_list:
            msg = "Not Found"
    return render(request, 'product/product.html', {'p_list': p_list, 'identity': identityCheck(request), 'message': msg, 'ss':ss})


def search_c(brand):
    searchBrand = product.objects.filter(brand=brand)
    return searchBrand


def search_vendor(data):
    searchPid = product.objects.filter(pid=data)
    searchPname = product.objects.filter(pname=data)
    if searchPid:
        return searchPid
    else:
        return searchPname


def ascending_product(p_list):
    p_list = p_list.order_by("price")
    return p_list


def descending_product(p_list):
    p_list = p_list.order_by("-price")
    return p_list


def product_detail(request, pid):
    row = product.objects.filter(pid=pid)
    detail = properties.objects.filter(pid=pid)
    # add a 'isInCart' parameter to check if the product in user's cart.
    return render(request, "product/detail.html", {'row': row, 'detail': detail, 'identity': identityCheck(request), 'isInCart': inCartCheck(request, pid)})


# return 0 if product not in cart, 1 if product in cart, 2 if user has not login, 3 if user is the vendor
def inCartCheck(request, po):
    if 'UserID' not in request.session:
        return 2
    if request.session['isVendor'] == 1:
        return 3
    uID = request.session['UserID']
    if shopcartRecord.objects.filter(aid=uID, pid=po):
        return 1
    else:
        return 0


def store_row(id_list):
    sort_list = []
    for id in id_list:
        po = product.objects.get(pid=id)
        sort_list.append(po)
    return sort_list


def practice(request):
    p_list = product.objects.filter(pid=1)
    return render(request, "product/practice.html", {"p_list": p_list})



