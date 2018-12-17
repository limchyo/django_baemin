from django.db import models
from django.contrib.auth.models import User
from partner.models import Menu

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    order_menu = models.ManyToManyField(
        Menu,
        through='OrderMenu',
        through_fields=('order', 'menu'),
    )
    
    def __str__(self):
        return ("주문자:{}, 주소:{}").format(self.client.name, self.address)

class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return ("주문자:{}, 메뉴:{}").format(self.order.client, self.menu.name)
