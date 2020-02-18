import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *

orderCount = 0


def addToCart(request, pid):
    shopcartRecord.objects.create(pid=product.objects.get(pid=pid),
                                  aid=account.objects.get(aid=request.session['UserID']), quantity=1)
    return HttpResponseRedirect('/productDetail/' + pid)


def cartListing(request):
    uID = request.session['UserID']
    recordList = shopcartRecord.objects.filter(aid=uID)
    productList = []
    for r in recordList:
        productList.append([shopcartRecord.objects.get(pid=r.pid), r.quantity])
    return render(request, 'Cart/CartPage.html', {'pList': productList})


def updateQuantity(request, pid):
    record = shopcartRecord.objects.get(aid=request.session['UserID'], pid=pid)
    record.quantity = request.GET['quan']
    record.save()
    return HttpResponseRedirect('/cart/')


def removeItem(request, pid):
    shopcartRecord.objects.get(aid=request.session['UserID'], pid=pid).delete()
    return HttpResponseRedirect('/cart/')


def checkOut(request):
    uID = request.session['UserID']
    productList = shopcartRecord.objects.filter(aid=uID)
    if not productList:
        return HttpResponse('Your cart is empty')
    global orderCount
    orderCount += 1
    newPO = 'po%05d' % orderCount
    tAmount = 0
    newPurchOrder = purchOrder.objects.create(po=newPO, pDate=datetime.datetime.now(), totalAmount=0, status='p',
                                              cancelledPerson='c', aid=account.objects.get(aid=uID),
                                              specDate=datetime.datetime.now())
    for p in productList:
        prod = p.pid
        dorder.objects.create(rName=prod.pname, rAddress=account.objects.get(aid=uID).saddress,
                              rQuentity=p.quantity, rPrice=prod.price, pid=prod, po=newPurchOrder)
        tAmount += prod.price * p.quantity
        p.delete()
    newPurchOrder.totalAmount = tAmount
    newPurchOrder.save()
    return HttpResponseRedirect('/order_detail/' + newPO)
