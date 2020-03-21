import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *
from mall.account import identityCheck

reviewCount = 0


def reviewUpdate(request):
    pid = request.POST['PID']
    po = request.POST['PO']
    rating = request.POST['Rating']
    reviewText = request.POST['Review']
    reviewRow = review.objects.filter(pid=pid, po=po)

    # review update
    if reviewRow:
        reviewRow[0].rating = rating
        reviewRow[0].review = reviewText
        reviewRow[0].modify_date = datetime.datetime.now()
        reviewRow[0].save()

    # review create
    else:

        # database review number check
        global reviewCount
        lastReview = review.objects.all().order_by('rid').last()
        if lastReview is not None:
            reviewCount = int(lastReview.rid) + 1
        else:
            reviewCount += 1

        review.objects.create(rid=reviewCount, rating=rating, review=reviewText, pid=product.objects.get(pid=pid),
                              po=purchOrder.objects.get(po=po), create_date=datetime.datetime.now())

    return HttpResponseRedirect('/order_detail/'+po)
