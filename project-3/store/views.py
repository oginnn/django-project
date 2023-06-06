from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .utils import cartData, guestOrder
from django.views.generic import DetailView
import json
import datetime
# Create your views here.
# class productDetail(DetailView):
#     model = Product
#     template_name = 'store/product_detail.html'
#     context_object_name = 'product'

def productDetail(request, slugInput):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.get(slug=slugInput)
    print(products)
    context = {
        'products': products,
        'cartItems' : cartItems,
    }
    return render(request, 'store/product_detail.html', context)

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {
        'page_title': 'OOPSHOODIE',
        'products': products,
        'cartItems':cartItems,
    }
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'page_title': 'Cart',
        'cartItems': cartItems,
        'items' : items,
        'order': order,
        }
    
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'page_title': 'Checkout',
        'items' : items,
        'order': order,
        'cartItems':cartItems,
        }
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action: ', action)
    print('productId: ',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)
        
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                kelurahan = data['shipping']['kelurahan'],
                kecamatan = data['shipping']['kecamatan'],
                city = data['shipping']['city'],
                zipcode = data['shipping']['zipcode'],
            )

    return JsonResponse('Payment completed...', safe=False)