from django.shortcuts import render
from ISI.models import product, properties, shopcartRecord
import decimal

def product_list(request):
    p_list = product.objects.all()
    return render(request, 'product/product.html', {'p_list':p_list, 'id': id})


def paging(request, id):
    p_list = product.objects.all()
    return render(request, 'product/product.html', {'p_list': p_list, 'id': id})


def filter_product(request):
    data = request.POST.get("find")
    search = product.objects.filter(brand=data)
    if search:
        return render(request, 'product/Search.html', {'search': search})
    else:
        msg = "No Finding"
        return render(request, 'product/Search.html', {'Error': msg})


def sort_product(request):
    fprice = decimal.Decimal(request.POST.get('fprice'))
    lprice = decimal.Decimal(request.POST.get('lprice'))
    allprice = product.objects.values_list('pid', 'price')
    msg = ''
    id_list = []
    sort_list = []
    if fprice >= lprice:
        msg = 'input error'
    else:
        id_list = sort_price(fprice, lprice, allprice)
        if id_list:
            sort_list = store_row(id_list)
        else:
            msg = 'No Finding'
    return render(request, "product/sort.html", {'message': msg, 'sort_list': sort_list})


def product_detail(request, pid):
    row = product.objects.filter(pid=pid)
    detail = properties.objects.filter(pid=pid)
    # add a 'isInCart' parameter to check if the product in user's cart.
    return render(request, "product/detail.html", {'row': row, 'detail': detail, 'isInCart': inCartCheck(request, pid)})


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




