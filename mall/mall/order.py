import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *
from mall.account import identityCheck


def orderListing(request):
    if identityCheck(request) == 0:
        return render(request, 'MessagePage.html', {'message': 'You need to login!', 'link': 'login'})
    if identityCheck(request) == 2:
        return orderListForVendor(request)

    uID = request.session['UserID']
    allOrderSet = purchOrder.objects.filter(aid=uID).order_by('-pDate')
    return render(request, 'Orders/PurchaseTracking.html', {'orderSet': allOrderSet,
                                                            'identity': identityCheck(request)})


def orderListForVendor(request):
    orderSet = purchOrder.objects.all().order_by('-pDate')
    return render(request, 'Orders/PurchaseOrderPageForVendor.html', {'orderSet': orderSet,
                                                                      'identity': identityCheck(request)})


def searchOrder(request):
    if identityCheck(request) != 2:
        return render(request, 'MessagePage.html', {'message': 'You are not vendor!', 'link': 'previous'})
    return orderDetail(request, request.GET['po'])


def orderDetail(request, PO):
    if identityCheck(request) == 0:
        return render(request, 'MessagePage.html', {'message': 'You need to login!', 'link': 'login'})
    try:
        order = purchOrder.objects.get(po=PO)
    except purchOrder.DoesNotExist:
        return render(request, 'MessagePage.html', {'message': 'Order does not exist!', 'link': 'previous'})
    productList = list(dorder.objects.filter(po=order))

    # search reviews for each product and combine them into an array
    n = 0
    for p in productList:
        pReview = review.objects.filter(pid=p.pid, po=p.po)
        if pReview:
            productList[n] = [p, pReview[0]]
            n += 1
        else:
            productList[n] = [p, '']
            n += 1
    return render(request, 'Orders/OrderDetail.html', {'order': order, 'pList': productList,
                                                       'identity': identityCheck(request)})


def shipOrder(request, PO):
    if identityCheck(request) != 2:
        return render(request, 'MessagePage.html', {'message': 'You are not vendor!', 'link': 'previous'})
    order = purchOrder.objects.get(po=PO)
    order.status = 's'
    order.specDate = datetime.datetime.now()
    order.save()
    return HttpResponseRedirect('/order_detail/' + PO)






