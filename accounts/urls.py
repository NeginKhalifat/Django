from django.urls import path,include
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/',views.logIn,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logOut,name='logout')



]