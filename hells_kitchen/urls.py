from django.urls import path
from . import views




urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.food_menu, name='menu'),
    path('menu/<int:dish_id>/',views.dish_details,name='dish_details'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('contactus/',views.contact_us,name='contactus')
]
