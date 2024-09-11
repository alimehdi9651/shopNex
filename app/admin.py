from django.contrib import admin
from .models import *

# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality','city', 'zipcode', 'state']
admin.site.register(Customer, CustomerModelAdmin)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'category', 'brand', 'discription',
                    'product_image']
admin.site.register(Product, ProductModelAdmin)

class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
admin.site.register(Cart, CartModelAdmin)

class OrderedPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','customer', 'quantity', 'status','order_date']
admin.site.register(OrderedPlaced)

