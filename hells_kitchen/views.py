from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Menu
from order.models import Cart

def homepage(request):
    return render(request,'hells_kitchen/homepage.html')

def food_menu(request):
    all_dishes=Menu.objects.all()
    cart_list=Cart.objects.filter(user=request.user)

    dish_quantities = {item.dish.id: item.quantity for item in cart_list}

    for dish in all_dishes:
        dish.quantity = dish_quantities.get(dish.id,0)

    return render(request,'hells_kitchen/menu.html',{'menu':all_dishes,})

def dish_details(request,dish_id):
    dish=get_object_or_404(Menu,pk=dish_id)
    return render(request,'hells_kitchen/dish_details.html',{'dish':dish})

def about_us(request):
    return render(request,'hells_kitchen/aboutus.html')

def contact_us(request):
    return render(request,'hells_kitchen/contactus.html')



