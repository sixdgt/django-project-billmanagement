from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the Bill Management Application!")
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')