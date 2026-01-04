from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the Bill Management Application!")
    return render(request, 'dashboard.html')

def product(request):
    return render(request, 'product.html')

def customer(request):
    return render(request, 'customer.html')

def report(request):
    return render(request, 'report.html')

def customer_create(request):
    return render(request, 'customers/customer_create.html')