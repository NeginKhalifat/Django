from django.shortcuts import render,redirect

from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")