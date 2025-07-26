from django.db import models

# Create your models here.
class Menu(models.Model):

    status_choice=[
        ("Veg","Vegetarian"),
        ("Non-Veg","Non-Vegetarian")
    ]
    
    dish=models.CharField(max_length=20,blank=False)
    price=models.IntegerField(blank=False)
    image=models.ImageField(upload_to='menu_images/',blank=True,null=True)
    ingredients=models.CharField(max_length=100,blank=True)
    status=models.CharField(max_length=10,choices=status_choice)
    description=models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.dish

