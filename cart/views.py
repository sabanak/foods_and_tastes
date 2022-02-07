from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,tot=0,count=0,ct_items=None):#for displaying cart details
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quantity)
            count +=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html",{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):#we create session key for each id
    ct_id=request.session.session_key                   #requesting cart id for a session
    if not ct_id:                                       #if there is no session key for cart id we need to create one
        ct_id=request.session.create()                  #here we create new session key
    return ct_id                                      #we need to call this returned cart id in everywhere

def add_cart(request,product_id):#for adding products to cart
    prod=products.objects.get(id=product_id)#next we need to call product id for adding to cart from shop app model import it
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))#here we call the cart id created in function cart_id ,that ct_id will be saved into models.py carlist's cart_id
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
               c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')

def min_cart(request,product_id):#for decrementing item from cart
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):#for deleting cart item
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')



