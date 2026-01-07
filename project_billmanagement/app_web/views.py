from django.shortcuts import render
from django.http import HttpResponse
from app_web.forms import ProductCategoryForm, ProductForm
# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the Bill Management Application!")
    context = {
        "message": "Welcome to our system!", 
        "date": "2026/01/07",
        "product": {
            "title": "Electric Jug",
            "price": 450
        }
    }
    return render(request, 'dashboard.html', context)

def product_category_create(request):
    form = ProductCategoryForm()
    context = {
        "category_form": form
    }
    return render(request, 'categories/product_category_create.html', context)

def product(request):
    return render(request, 'product.html')

def customer(request):
    return render(request, 'customer.html')

def report(request):
    return render(request, 'report.html')

def customer_create(request):
    return render(request, 'customers/customer_create.html')