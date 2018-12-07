from django.contrib import admin
from .models import Client, Order, OrderMenu

@admin.register(Client, Order, OrderMenu)
class ClientAdmin(admin.ModelAdmin):
    pass
