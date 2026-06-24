from django.contrib import admin
from .models import Customer, Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city']
admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'price', 'procust']
admin.site.register(Product, ProductAdmin)
