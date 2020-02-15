from django.shortcuts import render
from ISI.models import product, properties
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


def product_detail(request, name):
    row = product.objects.filter(thumbnail_image=name)
    po = row[0].pid
    detail = properties.objects.filter(pid=po)
    return render(request, "product/detail.html", {'row':row, 'detail': detail})


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




