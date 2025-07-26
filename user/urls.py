from django.urls import path
from . import views




urlpatterns = [
    path('register/', views.register, name='register'),
    path('loggedoutout/', views.logout_view, name='logoutview'),
    path('profile/',views.profile_view, name='profile'),

]
