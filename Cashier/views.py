from django.shortcuts import render, redirect
from django.http import HttpResponse

from Cashier.models import * 
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
    if request.method == "POST" and request.is_ajax():
        json_data = json.loads(request.body) 
        write_order_to_db(json_data)
        return HttpResponse("OK")
    else:
        return redirect('/')

def write_order_to_db(json_data):
    try:
        items = json_data['items']
    except KeyError:
        return None 

