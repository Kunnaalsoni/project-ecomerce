from django.contrib import admin
from commerce.models import Product, Category, Cart, OrderedDetails, Address
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(OrderedDetails)
admin.site.register(Address)
