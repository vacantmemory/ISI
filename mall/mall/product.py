from django.shortcuts import render
from ISI.models import product


def product_list(request):
    p_list = product.objects.all()
    return render(request, 'product.html', {'p_list':p_list})

def filter_product(request):
    data = request.POST.get("find")
    search = product.objects.filter(brand=data)
    if search:
        return render(request, 'Search.html', {'search': search})
    else:
        msg = "No Finding"
        return render(request, 'Search.html', {'Error': msg})