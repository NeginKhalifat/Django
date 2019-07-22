from django.urls import path,include
from . import views

app_name = 'vehicles'
urlpatterns = [

    path('car/',views.CarList,name="car"),
    path('motorcycle/',views.MotorList,name="motorcycle"),
    

]