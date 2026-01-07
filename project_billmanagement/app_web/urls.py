from django.urls import path
from app_web.views import (
    index, customer, customer_create, report, product,
    product_category_create
)

urlpatterns = [
    path('dashboard/', index, name="index"),
    path('customer/', customer, name='customer_page'),
    path('customer/create/', customer_create, name='customer_create'),
    path('report/', report, name='report_page'),
    path('product/', product, name='product_page'),
    path('product-category/create/', product_category_create, name='product_category_create'),
]