from django.shortcuts import render,redirect
from django.http import HttpResponse
from web import urls
# Create your views here.
def CarList(request):
    return HttpResponse('carlist')

def MotorList(request):
    return redirect('web:home')