from django.shortcuts import render
from ISI.models import product


def product_list(request):
    p_list = product.objects.all()
    p1 = []
    p2 = []
    p1.append(p_list[0])
    p2.append(p_list[1])
    return render(request, 'product.html', {'p1':p1, 'p2':p2})

def upload(request):
    image_file = request.FILES['images'].file.read()
    p1 = product.objects.get(pid='1')
    p1.thumbnail_image = image_file
    return render(request, 'FInish.html', {'ok':'Finish'})

def filter_product(request):
    data = request.POST.get("find")
    search = product.objects.filter(brand=data)
    if search:
        return render(request, 'FInish.html', {'search': search})
    else:
        msg = "No Finding"
        return render(request, 'FInish.html', {'Error': msg})