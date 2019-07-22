from django.urls import path,include
from . import views
app_name = 'main'
urlpatterns = [

    path('vehicles/',include('vehicles.urls'),name="vehicles"),
    
    #path('sport-entertainment/',include('sport-entertainment'),name='sport-entertainment'),
    #path('food-beverage/',include('food-beverage'),name='detail'),
    #path('apparel/',include('apparel'),name='detail')


]