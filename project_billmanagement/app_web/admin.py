from django.contrib import admin
from .models import ProductCategory, Product, ProductPriceHistory, ProductImages, Customer, ProductInvoice

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductPriceHistory)
admin.site.register(ProductImages)
admin.site.register(Customer)
admin.site.register(ProductInvoice)
