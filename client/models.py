from django.db import models
from django.contrib.auth.models import User
from partner.models import Menu

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    order_menu = models.ManyToManyField(Menu)
