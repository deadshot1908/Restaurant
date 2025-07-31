from django.shortcuts import render,get_object_or_404, redirect
from .models import Cart
from hells_kitchen.models import Menu
# Create your views here.


def add_to_cart(request,id):
    dish = get_object_or_404(Menu, pk=id)
    cart_item,created= Cart.objects.get_or_create(user=request.user, dish=dish)

    if not created:
        cart_item.quantity +=1
    cart_item.save()

    next_url = request.GET.get('next','menu')
    return redirect(next_url)


def remove_from_cart(request,id):
    dish = get_object_or_404(Menu,pk=id)
    item = get_object_or_404(Cart, dish=dish, user=request.user)

    if item.quantity == 1:
        item.delete()

    else:
        item.quantity -=1
        item.save()

    next_url = request.GET.get('next','menu')
    return redirect(next_url)

def view_cart(request):
    dishes = Cart.objects.filter(user=request.user)
    grandtotal = 0
    for dish in dishes:
        dish.totalprice = dish.dish.price * dish.quantity
        grandtotal += dish.totalprice
    return render(request,"order/view_cart.html",{'dishes':dishes,
                                                  'grandtotal':grandtotal})