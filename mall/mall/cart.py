import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *
from mall.account import identityCheck

orderCount = 0


def addToCart(request, pid):
    if identityCheck(request) == 0:
        return render(request, 'LoginNeededPage.html')
    if identityCheck(request) == 2:
        return HttpResponse('You are vendor!')

    shopcartRecord.objects.create(pid=product.objects.get(pid=pid),
                                  aid=account.objects.get(aid=request.session['UserID']), quantity=1)
    return HttpResponseRedirect('/productDetail/' + pid)


def cartListing(request):
    if identityCheck(request) == 0:
        return render(request, 'LoginNeededPage.html')
    if identityCheck(request) == 2:
        return HttpResponse('You are vendor!')

    uID = request.session['UserID']
    recordList = shopcartRecord.objects.filter(aid=uID)
    productList = []
    for r in recordList:
        productList.append([shopcartRecord.objects.get(pid=r.pid), r.quantity])
    return render(request, 'Cart/CartPage.html', {'pList': productList})


def updateQuantity(request, pid):
    if identityCheck(request) == 0:
        return render(request, 'LoginNeededPage.html')
    if identityCheck(request) == 2:
        return HttpResponse('You are vendor!')

    record = shopcartRecord.objects.get(aid=request.session['UserID'], pid=pid)
    record.quantity = request.GET['quan']
    record.save()
    return HttpResponseRedirect('/cart/')


def removeItem(request, pid):
    if identityCheck(request) == 0:
        return render(request, 'LoginNeededPage.html')
    if identityCheck(request) == 2:
        return HttpResponse('You are vendor!')

    shopcartRecord.objects.get(aid=request.session['UserID'], pid=pid).delete()
    return HttpResponseRedirect('/cart/')


def checkOut(request):
    # identity check
    if identityCheck(request) == 0:
        return render(request, 'LoginNeededPage.html')
    if identityCheck(request) == 2:
        return HttpResponse('You are vendor!')

    # cart check
    uID = request.session['UserID']
    productList = shopcartRecord.objects.filter(aid=uID)
    if not productList:
        return HttpResponse('Your cart is empty')

    # database po number check
    global orderCount
    lastOrder = purchOrder.objects.all().order_by('po').last()
    if lastOrder is not None:
        orderCount = int(lastOrder.po[-5:]) + 1
    else:
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
