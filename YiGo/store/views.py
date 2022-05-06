from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

import datetime
from .models import *
from .utils import cartData, orderData


def store(request):
    data = cartData(request)
    products = Product.objects.all()

    context = {'products': products, 'cartItems': data['cartItems']}

    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    
    context = data

    return render(request, 'store/cart.html', context)


def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('productID:', productID, 'action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def checkout(request):

    data = cartData(request)
    print('checkout data = ', data)

    context = {'items': data['items'], 'order': data['order'], 'cartItems':data['cartItems']}

    return render(request, 'store/checkout.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    form = json.loads(request.body)
    orderdata = orderData(request)
    print('processOrder data = ', form)
    print('order data = ', orderdata)
    total = orderdata['total']
    order = orderdata['order']
    customer = orderdata['customer']
    print('-'*18)
    print('total = ', total, 'order total = ', order.get_cart_total)
    print('total items =', order.get_cart_items)
    print('-'*18)
    if float(total) == float(order.get_cart_total):
        print('Total is correct')
        order.complete = True
    order.transaction_id = transaction_id
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer= customer,
            order=order,
            address=form['shipping']['address'],
            city=form['shipping']['city'],
            state=form['shipping']['state'],
            zipcode=form['shipping']['zipcode'],
        )

    return JsonResponse('You are all set', safe=False)
