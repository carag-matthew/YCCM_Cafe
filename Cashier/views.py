from django.shortcuts import render
from django.http import HttpResponse

from Cashier.models import Product, ProductMod


def index(request):
    inventory_list = Product.objects.order_by('-name').reverse()[:]
    mods_list = ProductMod.objects.order_by('-name').reverse()[:]

    context = {
        'inventory_list': inventory_list,
        'mods_list': mods_list
    }

    return render(request, 'cashier/index.html', context)
