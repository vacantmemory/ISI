from django.http import HttpResponse
from django.shortcuts import render
from ISI.models import *
from mall.account import *
from mall.order import *


def greeting(request):

    dorder.objects.all().delete()
    purchOrder.objects.all().delete()
    shopcartRecord.objects.all().delete()
    account.objects.all().delete()
    properties.objects.all().delete()
    product.objects.all().delete()

    p1 = product.objects.create(pid='1', pname='bible', brand='CTS', price=12.95, thumbnail_image='bible')
    product.objects.create(pid='2', pname='Harry Potter', brand='fiction', price=4.50, thumbnail_image='fiction')
    product.objects.create(pid='3', pname='dictionary', brand='fiction', price=4.50, thumbnail_image='dictionary')

    properties.objects.create(pid=p1, author='Derek', numPage=2000, publisher='xxxxx')

    a123 = account.objects.create(aid='account1', aname='Bowie', eaddress='P123366@ipm.edu.mo', password='44455666',
                           saddress='XXXXXXX', venderFlag=0)

    shopcartRecord.objects.create(pid=p1, aid=a123, quantity=10000)

    po123 = purchOrder.objects.create(po='purchOrder1', aid=a123, pDate='2021-02-01', totalAmount='200', status='p',
                                    specDate='2021-02-02', cancelledPerson='c')

    dorder.objects.create(po=po123, pid=p1, rName='Derek', rAddress='XXXX', rQuentity=10000,
                          rPrice=20.5)

    return HttpResponse('<h3>ok</h3>')


def test(request):
    # a123 = account.objects.get(aid='account1')
    # purchOrder.objects.create(po='purchOrder2', aid=a123, pDate='2019-02-01', totalAmount='300', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    # purchOrder.objects.create(po='purchOrder3', aid=a123, pDate='2020-02-01', totalAmount='500', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    return HttpResponse('ok')
