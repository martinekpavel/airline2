from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . formular import *
from django.shortcuts import render, redirect # přidáme redirect
from django.contrib.auth.forms import *

# Create your views here.
def user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
    else:
        form = RegistrationForm()
    
    return render(request, "users\sign_up.html", {
        "form":form
        })