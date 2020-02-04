from django.http import HttpResponse

def greeting(request):
    html = '<h3>Hello world</h3>'
    return HttpResponse(html)