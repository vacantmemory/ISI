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

    p1 = product.objects.create(pid='1', pname='Bible', brand='Education', price=120, thumbnail_image='bible')
    p2 = product.objects.create(pid='2', pname='Harry Potter', brand='Fiction', price=75, thumbnail_image='fiction')
    product.objects.create(pid='3', pname='Dictionary', brand='Reference', price=240, thumbnail_image='dictionary')
    product.objects.create(pid='4', pname='Steve Jobs', brand='Biography', price=170, thumbnail_image='Steve')
    product.objects.create(pid='5', pname='Albert Einstein', brand='Biography', price=150, thumbnail_image='Einstein')

    properties.objects.create(pid=p1, author='Derek', numPage=2000, publisher='xxxxx')

    a123 = account.objects.create(aid='account1', aname='Bowie', eaddress='P123366@ipm.edu.mo', password='44455666',
                           saddress='XXXXXXX', venderFlag=0)
    account.objects.create(aid='admin', aname='vendor', eaddress='vendor6@ipm.edu.mo', password='123',
                                  saddress='--', venderFlag=1)

    shopcartRecord.objects.create(pid=p1, aid=a123, quantity=10000)

    po1 = purchOrder.objects.create(po='po00001', aid=a123, pDate='2021-02-01', totalAmount='200', status='p',
                                    specDate='2021-02-02', cancelledPerson='c')
    po2 = purchOrder.objects.create(po='po00002', aid=a123, pDate='2019-02-02', totalAmount='400', status='h',
                                      specDate='2022-02-02', cancelledPerson='c')
    po3 = purchOrder.objects.create(po='po00003', aid=a123, pDate='2020-03-01', totalAmount='500', status='c',
                                      specDate='2024-02-02', cancelledPerson='c')

    dorder.objects.create(po=po1, pid=p1, rName='product1', rAddress='XXXX', rQuentity=10000,
                          rPrice=20.5)
    dorder.objects.create(po=po1, pid=p2, rName='product2', rAddress='YYYY', rQuentity=400,
                          rPrice=80.3)

    return HttpResponse('<h3>ok</h3>')


def test(request):
    # a123 = account.objects.get(aid='account1')
    # purchOrder.objects.create(po='purchOrder2', aid=a123, pDate='2019-02-01', totalAmount='300', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    # purchOrder.objects.create(po='purchOrder3', aid=a123, pDate='2020-02-01', totalAmount='500', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    return HttpResponse('ok')
