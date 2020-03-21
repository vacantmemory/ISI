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
    p3 = product.objects.create(pid='3', pname='Oxford', brand='Reference', price=240, thumbnail_image='oxford')
    p4 = product.objects.create(pid='4', pname='Steve Jobs', brand='Biography', price=170, thumbnail_image='Steve')
    p5 = product.objects.create(pid='5', pname='Albert Einstein', brand='Biography', price=150, thumbnail_image='Einstein')
    p6 = product.objects.create(pid="6", pname="Cambridge", brand='Reference', price=279, thumbnail_image='cambridge')
    p7 = product.objects.create(pid="7", pname="WinterStory", brand='Story', price=90, thumbnail_image='winterStory')
    p8 = product.objects.create(pid="8", pname="russianStory", brand='Story', price=190, thumbnail_image='russianStory')
    p9 = product.objects.create(pid="9", pname="bibleStory", brand='Story', price=290, thumbnail_image='bibleStory')
    p10 = product.objects.create(pid="10", pname="animal", brand='Story', price=280, thumbnail_image='animal')

    properties.objects.create(pid=p1, author='Derek', numPage=2000, publisher='xxxxx')
    properties.objects.create(pid=p2, author='Bowie', numPage=1900, publisher='ppp')
    properties.objects.create(pid=p3, author='Neil', numPage=1800, publisher='llll')
    properties.objects.create(pid=p4, author='David', numPage=1760, publisher='ddd')
    properties.objects.create(pid=p5, author='Franz', numPage=2450, publisher='sss')
    properties.objects.create(pid=p6, author='Kidney', numPage=1360, publisher='cc')
    properties.objects.create(pid=p7, author='Bob', numPage=1230, publisher='zz')
    properties.objects.create(pid=p8, author='Cindy', numPage=1120, publisher='dd')
    properties.objects.create(pid=p9, author='Dandy', numPage=1340, publisher='ee')
    properties.objects.create(pid=p10, author='Lisa', numPage=1890, publisher='ff')

    a123 = account.objects.create(aid='account1', aname='Bowie', eaddress='P123366@ipm.edu.mo', password='44455666',
                           saddress='XXXXXXX', venderFlag=0)

    account.objects.create(aid='admin', aname='vendor', eaddress='vendor6@ipm.edu.mo', password='123',
                                  saddress='--', venderFlag=1)

    shopcartRecord.objects.create(pid=p1, aid=a123, quantity=10000)

    po1 = purchOrder.objects.create(po='po00001', aid=a123, pDate='2020-02-01', totalAmount='200', status='p',
                                    specDate='2021-02-02', cancelledPerson='c')
    po2 = purchOrder.objects.create(po='po00002', aid=a123, pDate='2019-02-02', totalAmount='400', status='h',
                                      specDate='2022-02-02', cancelledPerson='c')
    po3 = purchOrder.objects.create(po='po00003', aid=a123, pDate='2020-03-01', totalAmount='500', status='c',
                                      specDate='2024-02-02', cancelledPerson='c')

    dorder.objects.create(po=po1, pid=p1, rName='product1', rAddress='XXXX', rQuentity=10000,
                          rPrice=20.5)
    dorder.objects.create(po=po1, pid=p2, rName='product2', rAddress='YYYY', rQuentity=400,
                          rPrice=80.3)

    review.objects.create(rid=1, po=po1, pid=p1, rating=4, review='very good!', create_date='2020-3-10')

    return HttpResponse('<h3>ok</h3>')


def test(request):
    # a123 = account.objects.get(aid='account1')
    # purchOrder.objects.create(po='purchOrder2', aid=a123, pDate='2019-02-01', totalAmount='300', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    # purchOrder.objects.create(po='purchOrder3', aid=a123, pDate='2020-02-01', totalAmount='500', status='p',
    #                           specDate='2021-02-02', cancelledPerson='c')
    return HttpResponse('ok')
