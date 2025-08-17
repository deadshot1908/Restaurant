from django.db import models
from django.contrib.auth.models import User
from hells_kitchen.models import Menu
from django.utils import timezone

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='cart_items')
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.dish.dish} by {self.user.username}"
    

class Order(models.Model):

    status_choices=[
        ('pending','pending'),
        ('accepted','accepted'),
        ('delieverd','delieverd'),
        ('cancelled','cancelled')
    ]
    order_id = models.CharField(max_length=12, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    amount = models.PositiveBigIntegerField()
    date_ordered = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=status_choices,default='pending')
    payment_mode = models.CharField(max_length=20)

    def __str__(self):
        return f"order no. {self.order_id} by {self.user.username}"
    
class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_item")
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.item.dish} of {self.order.order_id}"
    


    