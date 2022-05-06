import json
from abc import ABC, abstractmethod

from .models import *


class AbstractCartHandler(ABC):

    def __init__(self, request) -> None:
        self.request = request

    @abstractmethod
    def handleUserCartData(self):
        pass
    @abstractmethod
    def handleUserCheckoutData(self):
        pass

class AnonymousUserCartHandler(AbstractCartHandler):

    def handleUserCartData(self):
        try:
            cart = json.loads(self.request.COOKIES['cart'])
        except:
            cart = {}
        # print('Now cart = ', cart)
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                product_total = product.price * cart[i]['quantity']

                order['get_cart_total'] += product_total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                    'quantity': cart[i]['quantity'],
                    'get_total': product_total,
                    'digital': product.digital
                }
                product_context = ['id', 'name', 'price', 'imageURL']
                item['product'] = {name: getattr(
                    product, name) for name in product_context}
                items.append(item)

                if product.digital == False:
                    order['shipping'] = True
            except:
                pass

        return {'items': items, 'order': order, 'cartItems': cartItems}

    def handleUserCheckoutData(self):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(self.request.body)
        name = data['form']['name']
        email = data['form']['email']
        cookieData = cartData(self.request)
        print('cookieData:', cookieData)
        customer, created = Customer.objects.get_or_create(
            name=name,
            email=email,
        )
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in cookieData['items']:
            product = Product.objects.get(id=item['product']['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )

        return { 'customer':customer, 
                 'order': order, 
                 'total': data['form']['total']
                 }

    def __str__(self) -> str:
        return f"I am Anonymous User"

class AuthenticatedUserCartHandler(AbstractCartHandler):

    def handleUserCartData(self):
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        shipping = order.shipping

        return {'items': items, 'order': order, 'cartItems': cartItems}

    def handleUserCheckoutData(self):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(self.request.body)
        print('data=', data)
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        return { 'customer':customer, 
                 'order': order, 
                 'total': data['form']['total']
                 }

    def __str__(self) -> str:
        return f"I am Authenticated User"


def get_data_handler(request):

    switcher = {
            '0': AnonymousUserCartHandler,
            '1': AuthenticatedUserCartHandler,
            }

    user_category = '0'
    if request.user.is_authenticated:
        user_category = '1'

    handler = switcher.get(user_category, '0')
    print('handler = ', handler)
    return handler(request)

def cartData(request) -> dict:

    cartDataHandler = get_data_handler(request)

    return cartDataHandler.handleUserCartData()

def orderData(request) -> dict:
    
    orderDataHandler = get_data_handler(request)

    return orderDataHandler.handleUserCheckoutData()
    


    