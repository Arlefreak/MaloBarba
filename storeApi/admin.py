from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
        list_display = ('order', 'sku', 'name', 'inventory', 'price', 'status', 'date',)

class AdressAdmin(admin.ModelAdmin):
        list_display = ('user', 'name', 'type', 'default', 'country', 'zipcode')

admin.site.register(Product, ProductAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Client)
admin.site.register(Order)
