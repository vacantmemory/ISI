from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *


def orderListing(request):
    if 'UserID' not in request.session:
        message = 'You need to login!'
        return HttpResponse(message)
    uID = request.session['UserID']
    allOrderSet = purchOrder.objects.filter(aid=uID).order_by('-pDate')
    return render(request, 'PurchaseTracking.html', {'orderSet': allOrderSet})


def orderDetail(request, PO):
    try:
        order = purchOrder.objects.get(po=PO)
    except purchOrder.DoesNotExist:
        message = 'Error: Order does not exist!'
        return HttpResponse(message)
    return render(request, 'OrderDetail.html', {'order': order})




