from django.http import HttpResponse
from django.shortcuts import render
from ISI.models import *

def greeting(request):


    properties.objects.all().delete()
    account.objects.all().delete()
    shopcartRecord.objects.all().delete()
    purchOrder.objects.all().delete()
    dorder.objects.all().delete()
    product.objects.all().delete()

    p123 = product.objects.create(pid='123', pname='story', brand='xxx', price=20.5)

    properties.objects.create(pid=p123, author='Derek', numPage=2000, publisher='xxxxx')

    a123 = account.objects.create(aid='account1', aname='Bowie', eaddress='P123366@ipm.edu.mo', password='44455666',
                           saddress='XXXXXXX', venderFlag=0)


    shopcartRecord.objects.create(pid=p123, aid=a123, quantity=10000)

    po123 = purchOrder.objects.create(po='purchOrder1', aid=a123, pDate='2021-02-01', totalAmount='200', status='p',
                              specDate='2021-02-02', cancelledPerson='c')

    dorder.objects.create(po=po123, pid=p123, rName='Derek', rAddress='XXXX', rQuentity=10000,
                          rPrice=20.5)

    return HttpResponse('<h3>ok</h3>')