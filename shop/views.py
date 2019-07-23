from django.shortcuts import render,redirect

from django.http import HttpResponse
from math import ceil
from .models import Product
def index(request):
    products = Product.objects.all()
    print(products)
    allProds=[]
    catprod=Product.objects.values('category','id')
    cats={item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-n//4)
        allProds.append([prod,range(1,nslides),nslides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html',params)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")