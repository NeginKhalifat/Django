from django.urls import path,include
from . import views
app_name = 'stuff'
urlpatterns = [

    path('create/',views.Create,name="create"),
    path('<slug:slug>/',views.Stuff_Details,name='detail')



]