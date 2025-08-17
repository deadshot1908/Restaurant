from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Cart,Order,Order_item
from hells_kitchen.models import Menu
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request,id):
    dish = get_object_or_404(Menu, pk=id)
    cart_item,created = Cart.objects.get_or_create(user=request.user, dish=dish)

    if not created:
        cart_item.quantity +=1
    cart_item.save()

    next_url = request.GET.get('next','menu')
    return redirect(next_url)

@login_required
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

@login_required
def view_cart(request):
    dishes = Cart.objects.filter(user=request.user)
    grandtotal = 0
    for dish in dishes:
        dish.totalprice = dish.dish.price * dish.quantity
        grandtotal += dish.totalprice
    return render(request,"order/view_cart.html",{'dishes':dishes,
                                                  'grandtotal':grandtotal})

@login_required
def place_order(request):

    if request.method == 'POST':
        payment = request.POST.get("payment_method")
        dishes = Cart.objects.filter(user=request.user)
        grandtotal = 0
        for dish in dishes:
            dish.totalprice = dish.dish.price * dish.quantity
            grandtotal += dish.totalprice
            

        last_id = Order.objects.all().count()    
        order_id = 'ord' + str(last_id + 1)
        user = request.user
        amount = grandtotal
        order = Order.objects.create(order_id=order_id,user=user,amount=grandtotal,payment_mode=payment)
        for dish in dishes:
            Order_item.objects.create(order=order,item=dish.dish,quantity=dish.quantity)
        Cart.objects.filter(user=request.user).delete()
        return render(request,'order/orderconfirmation.html',{'order':order})

    dishes = Cart.objects.filter(user=request.user)
    if not dishes.exists():
            return redirect("menu")
    grandtotal = 0
    for dish in dishes:
        dish.totalprice = dish.dish.price * dish.quantity
        grandtotal += dish.totalprice

    return render(request,"order/place_order.html",{
                                                    'total':grandtotal,

    })

@login_required
def my_order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'order/myorder.html',{'orders':orders})

def order_details(request,order_id):
    order = get_object_or_404(Order,order_id=order_id)
    grandtotal = order.amount
    status = order.status
    order_items = Order_item.objects.filter(order=order)

    return render(request,'order/orderdetails.html',{'order_items':order_items,'grandtotal':grandtotal,'status':status})



@login_required
def check_or_add_address(request):
    if request.user.profile.Phone=='' or request.user.profile.Address=='' or request.user.profile.Name=='':
        next_url = reverse("checkprofile")
        return redirect(f"{reverse('profile')}?next={next_url}")
    
    return redirect("placeorder")

