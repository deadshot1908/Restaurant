from django.db import models
from django.contrib.auth.models import User
from hells_kitchen.models import Menu

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='cart_items')
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return f"{self.dish.dish} by {self.user.username}"