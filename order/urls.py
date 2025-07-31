from django.urls import path
from . import views




urlpatterns = [
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add to cart'),
    path('remove_from_cart/<int:id>/',views.remove_from_cart,name='remove from cart'),
    path('viewcart/',views.view_cart,name='viewcart'),

]
