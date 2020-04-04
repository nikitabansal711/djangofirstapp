from django.contrib import admin

from template.models import Customer, Product, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
