from django.shortcuts import render, redirect
from django.http import HttpResponse

from Cashier.models import Product, ProductMod
import json


def index(request):
    inventory_list = Product.objects.order_by('-name').reverse()[:]
    mods_list = ProductMod.objects.order_by('-name').reverse()[:]

    context = {
        'inventory_list': inventory_list,
        'mods_list': mods_list
    }

    return render(request, 'cashier/index.html', context)

def create_order(request):
    if request.method == "POST":
        print('*'*50)
        print(json.loads(request.body))
        print('*'*50)
    else:
        return redirect('/')
