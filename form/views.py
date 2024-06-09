from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

login_required(login_url="login")
def homes(request):
    return render(request,"Home.html")
def web(request):
    return render(request,"web.html")
def logins(request):
    if request.method=="POST":
        user_name1=request.POST.get('username')
        password1=request.POST.get('pass')
        user=authenticate(request,username=user_name1,password=password1)
        if user is not None:
            login(request,user)
            return redirect('/web/')
        else:
            return HttpResponse("password or username are incorect!!")
        


    return render(request,"login.html")

def sign(request): 
    if request.method=="POST":
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        conform_password=request.POST.get('password2')
        if password!=conform_password:
            return HttpResponseRedirect("password and conform password are not match")
        else:
            my_user=User.objects.create_user(user_name,email,password)
            my_user.save()
            return HttpResponseRedirect("/login/")
    return render(request,"singup.html")

def LogoutPage(request):
    logout(request)
    return redirect("/login/")

