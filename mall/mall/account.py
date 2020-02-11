from django.http import HttpResponse
from django.shortcuts import render
from ISI.models import *


def login(request):
    request.session.set_expiry(0)
    if 'UserID' in request.session:
        return render(request, 'HomePage.html')
    return render(request, 'LoginPage.html')


def loginCheck(request):

    if 'UserID' and 'UserPswd' in request.POST:
        uID = request.POST.get('UserID')
        uPswd = request.POST.get('UserPswd')
    else:
        message = 'Error: Incorrect Login Information!'
        return HttpResponse(message)

    try:
        account.objects.get(aid=uID, password=uPswd)
    # fill error type
    except account.DoesNotExist:
        message = 'Error: Incorrect Login Information!'
        return HttpResponse(message)
    request.session['UserID'] = uID
    return render(request, 'HomePage.html')

