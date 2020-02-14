import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *


def orderListing(request):
    if identityCheck(request) == 0:
        return HttpResponse('You need to login!')
    if identityCheck(request) == 2:
        return orderListForVendor(request)
    uID = request.session['UserID']
    allOrderSet = purchOrder.objects.filter(aid=uID).order_by('-pDate')
    return render(request, 'PurchaseTracking.html', {'orderSet': allOrderSet})


def orderListForVendor(request):
    orderSet = purchOrder.objects.all().order_by('-pDate')
    return render(request, 'PurchaseOrderPageForVendor.html', {'orderSet': orderSet})


def searchOrder(request):
    if identityCheck(request) != 2:
        return HttpResponse('You are not vendor!')
    return orderDetail(request, request.GET['po'])


def orderDetail(request, PO):
    if identityCheck(request) == 0:
        return HttpResponse('You need to login!')
    try:
        order = purchOrder.objects.get(po=PO)
    except purchOrder.DoesNotExist:
        message = 'Error: Order does not exist!'
        return HttpResponse(message)
    productList = dorder.objects.filter(po=order)
    return render(request, 'OrderDetail.html', {'order': order, 'pList': productList})


def shipOrder(request, PO):
    if identityCheck(request) != 2:
        return HttpResponse('You are not vendor!')
    order = purchOrder.objects.get(po=PO)
    order.status = 's'
    order.specDate = datetime.datetime.now()
    order.save()
    productList = dorder.objects.filter(po=order)
    return render(request, 'OrderDetail.html', {'order': order, 'pList': productList})


def identityCheck(request):
    if 'UserID' not in request.session:
        return 0
    if request.session['isVendor'] == 0:
        return 1
    else:
        return 2




