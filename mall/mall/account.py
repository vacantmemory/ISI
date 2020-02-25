from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ISI.models import *

# User id will be saved in session as 'UserID'

def login(request):
    request.session.set_expiry(0)
    if identityCheck(request):
        # return render(request, 'HomePage.html')
        return HttpResponseRedirect('/home/')
    return render(request, 'SignIn/LoginPage.html')


def signOut(request):
    request.session.flush()
    return HttpResponseRedirect('/login/')


def loginCheck(request):

    if request.POST['UserID'] != '' and request.POST['UserPswd'] != '':
        uID = request.POST['UserID']
        uPswd = request.POST['UserPswd']
    else:
        message = 'Error: Incorrect Login Information!'
        return HttpResponse(message)

    try:
        user = account.objects.get(aid=uID, password=uPswd)
    except account.DoesNotExist:
        message = 'Error: Something wrong!'
        return HttpResponse(message)
    request.session['UserID'] = uID
    request.session['isVendor'] = user.venderFlag
    request.session['UserName'] = user.aname
    # return render(request, 'HomePage.html')
    return HttpResponseRedirect('/home/')


def home(request):
    # identity = 0
    # if identityCheck(request) == 1:
    #     identity = 1
    # if identityCheck(request) == 2:
    #     identity = 2

    return render(request, 'HomePage.html', {"identity": identityCheck(request)})


def register(request):
    return render(request, 'SignIn/Register.html')


def registerSystem(request):

    if request.POST['UserID'] != '' and request.POST['UserPswd'] != '':
        uID = request.POST['UserID']
        uPswd = request.POST['UserPswd']
    else:
        message = 'Error: You need to fill both ID and password!'
        return HttpResponse(message)

    try:
        account.objects.get(aid=uID)
    except account.DoesNotExist:
        account.objects.create(aid=uID, password=uPswd, venderFlag=0)
        request.session['UserID'] = uID
        return render(request, 'SignIn/SignUpSuccessful.html')
    else:
        message = 'Error: User exist!'
        return HttpResponse(message)


# return 0 if user has not done login in, 1 if user is a customer, 2 if user is the vendor
def identityCheck(request):
    if 'UserID' not in request.session:
        return 0
    if request.session['isVendor'] == 0:
        return 1
    else:
        return 2
