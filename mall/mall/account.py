from django.http import HttpResponse
from django.shortcuts import render
from ISI.models import *


def login(request):
    request.session.set_expiry(0)
    if 'UserID' in request.session:
        return render(request, 'HomePage.html')
    return render(request, 'LoginPage.html')


def loginCheck(request):

    if request.POST['UserID'] != '' and request.POST['UserPswd'] != '':
        uID = request.POST['UserID']
        uPswd = request.POST['UserPswd']
    else:
        message = 'Error: Incorrect Login Information!'
        return HttpResponse(message)

    try:
        account.objects.get(aid=uID, password=uPswd)
    except account.DoesNotExist:
        message = 'Error: Something wrong!'
        return HttpResponse(message)
    request.session['UserID'] = uID
    return render(request, 'HomePage.html')


def home(request):
    return render(request, 'HomePage.html')


def register(request):
    return render(request, 'Register.html')


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
        return render(request, 'SignUpSuccessful.html')
    else:
        message = 'Error: User exist!'
        return HttpResponse(message)
