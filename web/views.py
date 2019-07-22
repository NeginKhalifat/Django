from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home.html')