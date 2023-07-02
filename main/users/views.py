from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index')
    else:
        form= UserRegistrationForm()
    return render(request,'users/signup.html',{'form':form})

# def profile(request,id):
#     user=User.objects.get(pk=id)
#     return render(request,'users/profile.html',{'user':user})

def userlogin(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return render(request,'users/profile.html',{'user':user})
            else:
                form.add_error(None,"Invalid Username or Password")
    else:
        form=UserLoginForm()
    return render(request, 'users/login.html',{'form':form})


def userlogout(request):
    logout(request)
    return redirect('userlogin')


