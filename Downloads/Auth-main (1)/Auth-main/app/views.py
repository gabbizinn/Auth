from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#MY PAGES

#Home Page function
def home(request):
    return render(request, "accounts/dashboard.html")

#Product Page Function
def product(request):
    return render(request, "accounts/product.html")

#Customer Page Function
def customer(request):
    return render(request, "accounts/customer.html")