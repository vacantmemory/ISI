from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *


# User information will be saved in session as 'UserID', 'UserName', 'isVendor'

def login(request):
    request.session.set_expiry(0)
    if identityCheck(request):
        return HttpResponseRedirect('/product/')
    return render(request, 'SignIn/LoginPage.html')


def signOut(request):
    request.session.flush()
    return HttpResponseRedirect('/login/')


def loginCheck(request):
    if request.POST['UserID'] != '' and request.POST['UserPswd'] != '':
        uID = request.POST['UserID']
        uPswd = request.POST['UserPswd']
    else:
        return render(request, 'MessagePage.html', {'message': 'Incorrect login information', 'link': 'previous'})

    try:
        user = account.objects.get(aid=uID, password=uPswd)
    except account.DoesNotExist:
        return render(request, 'MessagePage.html', {'message': 'Incorrect login information', 'link': 'previous'})
    request.session['UserID'] = uID
    request.session['isVendor'] = user.venderFlag
    request.session['UserName'] = user.aname
    return HttpResponseRedirect('/product/')


def home(request):
    return render(request, 'HomePage.html', {"identity": identityCheck(request)})


def register(request):
    return render(request, 'SignIn/Register.html')


def registerSystem(request):
    if request.POST['UserID'] and request.POST['UserPswd'] and request.POST['UserName'] and request.POST['UserEmail'] and request.POST['UserAddr']:
        uID = request.POST['UserID']
        uPswd = request.POST['UserPswd']
        uName = request.POST['UserName']
        uEmail = request.POST['UserEmail']
        uAddr = request.POST['UserAddr']
    else:
        return render(request, 'MessagePage.html',
                      {'message': 'You need to fill in all the information!', 'link': 'previous'})

    try:
        account.objects.get(aid=uID)
    except account.DoesNotExist:
        account.objects.create(aid=uID, password=uPswd, aname=uName, eaddress=uEmail, saddress=uAddr, venderFlag=0)
        request.session['UserID'] = uID
        request.session['isVendor'] = 0
        request.session['UserName'] = uName
        return render(request, 'MessagePage.html', {'message': 'Sign Up Successful!', 'link': 'product'})
    else:
        return render(request, 'MessagePage.html',
                      {'message': 'User already exists!', 'link': 'previous'})


# return 0 if user has not done login in, 1 if user is a customer, 2 if user is the vendor
def identityCheck(request):
    if 'UserID' not in request.session:
        return 0
    if request.session['isVendor'] == 0:
        return 1
    else:
        return 2
