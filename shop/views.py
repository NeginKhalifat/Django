from django.shortcuts import render,redirect

from django.http import HttpResponse
from math import ceil
from .models import Product
def index(request):
    products = Product.objects.all()

    allProds=[]
    catprod=Product.objects.values('category','id')
    cats={item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-n//4)
        allProds.append([prod,range(1,nslides),nslides])
    params = {'allProds':allProds}
   # print(allProds)
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
def tracker(request):
    return render(request,'shop/tracker.html')

def contact(request):
    return render(request,'shop/contact.html')

def productView(request,myid):
    product = Product.objects.filter(id=myid)
  
    return render(request,'shop/prodview.html',{'product':product[0]})


def search(request):
    return render(request,'shop/search.html')


def checkout(request):
    return render(request,'shop/checkout.html')
