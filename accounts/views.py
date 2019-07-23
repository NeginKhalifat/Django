from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout


def logIn(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('web:home')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
  



def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('web:home')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
    


def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('web:home')