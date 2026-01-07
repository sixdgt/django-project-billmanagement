from django import forms
from app_web.models import ProductCategory, Product, Customer

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'description']
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_title', 'product_category',\
                  'product_description', 'current_product_price',\
                      'tax_rate', 'product_status']