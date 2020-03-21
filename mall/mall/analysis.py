from django.shortcuts import render
from django.http import HttpResponse
from ISI.models import *
import html
import datetime
import pytz


def analysis(request):
    choose = request.POST.get("time")
    alter = request.POST.get("alter")
    #request.session['choose'] = choose
    list_sum = {}
    i = 1
    time = 30
    total = []
    if alter:
        time = 100
        #time = request.session['choose']
        book_name = order_a(time)
        text = 'Sales Amount'
        check = 'amount'
        for name in book_name:
            total_group = {}
            sum_group = {}
            sum, list = amount(name, time)
            # container
            sum_group['sum'] = sum
            sum_group['name'] = name
            sum_group['list'] = list
            list_sum[i] = sum_group
            # atable
            total_group['name'] = name
            total_group['sum'] = sum
            total.append(total_group)
            i += 1
    else:
        if choose:
            time = int(choose)
        book_name = order_q(time)
        text = 'Sales Quantity'
        check = 'quantity'
        for name in book_name:
            total_group = {}
            sum_group = {}
            sum, list = quantity(name, time)
            # container
            sum_group['sum'] = sum
            sum_group['name'] = name
            sum_group['list'] = list
            list_sum[i] = sum_group
            # atable
            total_group['name'] = name
            total_group['sum'] = sum
            total.append(total_group)
            i += 1
    return render(request, "Analysis.html", {"list_sum":list_sum, "text":text, "check": check, 'total': total})


def quantity(name, time):
    book = product.objects.get(pname=name).pid
    list_B = dorder.objects.filter(pid=book)
    list = []
    sum = 0
    for i in list_B:
        list_date = []
        quentity = i.rQuentity
        range = compare(i, time)
        if range:
            list_date.append(range)
            list_date.append(quentity)
            list.append(list_date)
            sum += quentity
    return sum, list


def amount(name, time):
    book = product.objects.get(pname=name).pid
    list_B = dorder.objects.filter(pid=book)
    list = []
    sum = 0
    for i in list_B:
        list_date = []
        price = i.rPrice
        quentity = i.rQuentity
        amount = int(price * quentity)
        range = compare(i, time)
        if range:
            list_date.append(range)
            list_date.append(amount)
            list.append(list_date)
            sum += amount
    return sum, list


def compare(i, time):
    date = purchOrder.objects.get(po=i.po_id).pDate
    range = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
    current = datetime.datetime.now()
    boundary = current - datetime.timedelta(time)
    utc = pytz.utc
    boundary = boundary.replace(tzinfo=utc)
    if date >= boundary:
        return range
    else:
        return False


def order_q(time):
    book_name = product.objects.values_list('pname', flat=True)
    list = {}
    for name in book_name:
        book = product.objects.get(pname=name).pid
        list_B = dorder.objects.filter(pid=book)
        sum = 0
        for i in list_B:
            quentity = i.rQuentity
            day = compare(i, time)
            if day:
                sum += quentity
        list[name] = sum
    list_order = {k: v for k, v in sorted(list.items(), key=lambda item: item[1], reverse=True)}
    order = []
    for i in list_order.keys():
        order.append(i)
    return order


def order_a(time):
    book_name = product.objects.values_list('pname', flat=True)
    list = {}
    for name in book_name:
        book = product.objects.get(pname=name).pid
        list_B = dorder.objects.filter(pid=book)
        sum = 0
        for i in list_B:
            quentity = i.rQuentity
            price = i.rPrice
            amount = int(price * quentity)
            day = compare(i, time)
            if day:
                sum += amount
        list[name] = sum
    list_order = {k: v for k, v in sorted(list.items(), key=lambda item: item[1], reverse=True)}
    order = []
    for i in list_order.keys():
        order.append(i)
    return order