from django.shortcuts import render
from ISI.models import product, properties, shopcartRecord
import decimal
from mall.account import identityCheck


def product_list(request):
    p_list = product.objects.all()
    return render(request, 'product/product.html', {'p_list':p_list, 'id': id})


def paging(request, id):
    p_list = product.objects.all()
    return render(request, 'product/product.html', {'p_list': p_list, 'id': id})


def search_product(request):
    data = request.POST.get("find")
    msg = "No Finding"
    if identityCheck(request) == 0 or identityCheck(request) == 1:
        searchBrand = product.objects.filter(brand=data)
        if searchBrand:
            return render(request, 'product/sort&search.html', {'searchBrand': searchBrand})
        else:
            return render(request, 'product/sort&search.html', {'Error': msg})
    if identityCheck(request) == 2:
        searchBrand = product.objects.filter(brand=data)
        searchPid = product.objects.filter(pid=data)
        searchPname = product.objects.filter(pname=data)
        if searchPid or searchPname or searchBrand:
            return render(request, 'product/sort&search.html', {'searchBrand': searchBrand, 'searchPid': searchPid, 'searchPname': searchPname})
        else:
            return render(request, 'product/sort&search.html', {'Error': msg})


def sort_product(request):
    fprice = decimal.Decimal(request.POST.get('fprice'))
    lprice = decimal.Decimal(request.POST.get('lprice'))
    allprice = product.objects.values_list('pid', 'price')
    msg = ''
    sort_list = []
    if fprice >= lprice:
        msg = 'input error'
    else:
        id_list = sort_price(fprice, lprice, allprice)
        if id_list:
            sort_list = store_row(id_list)
        else:
            msg = 'No Finding'
    return render(request, "product/sort&search.html", {'message': msg, 'sort_list': sort_list})


def product_detail(request, pid):
    row = product.objects.filter(pid=pid)
    detail = properties.objects.filter(pid=pid)
    identity = 0
    if identityCheck(request) == 0:
        identity = 0
    if identityCheck(request) == 1:
        identity = 1
    if identityCheck(request) == 2:
        identity = 2
    # add a 'isInCart' parameter to check if the product in user's cart.
    return render(request, "product/detail.html", {'row': row, 'detail': detail, 'identity': identity, 'isInCart': inCartCheck(request, pid)})


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





def sort_price(fprice, lprice, allprice):
    id_list = []
    for i in allprice:
        if i[1] > fprice and i[1] <= lprice:
            id_list.append(i[0])
        else:
            continue
    return id_list


def store_row(id_list):
    sort_list = []
    for id in id_list:
        po = product.objects.get(pid=id)
        sort_list.append(po)
    return sort_list




