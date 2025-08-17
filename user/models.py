from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=25, blank=True)
    Phone = models.CharField(max_length=10, blank=True)
    Address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    