from django.shortcuts import render
from django.http import HttpResponse

from Cashier.models import Product


def index(request):
    inventory_list = Product.objects.order_by('-price')[:5]
    context = {'inventory_list': inventory_list}
    return render(request, 'cashier/index.html', context)
