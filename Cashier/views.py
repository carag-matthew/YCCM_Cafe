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
        customerName = json_data['customerName']
        price = json_data['totalPrice']
        paidByCard = json_data['paidByCard']

        orderitem_mods_list = []
        
        for item in items:
            orderItem = OrderItem(customer=customerName, paidByCard=paidByCard) 
            print(item)
            # Add Product to OrderItem
            product = Product.objects.get(name=item['name'])
            orderItem.product = product
            orderItem.quantity = item['quantity']
            orderItem.price = item['price']
            orderItem.save()

            if len(item['mods']) > 0:
                orderitem_mods = OrderItem_Mods()
                for mod in item['mods']:
                    productMod = ProductMod.objects.get(name=mod['name'])
                    orderitem_mods.mod = productMod
                    orderitem_mods.quantity = mod['quantity']
                    orderItem.price = orderItem.price + (mod['price'] * mod['quantity'])
                    orderitem_mods.save()
                    orderItem.product_mods.add(orderitem_mods)
                    orderItem.save()


    except KeyError:
        return None 

