from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)

    ctx = {}
    return render(request, "signup.html", ctx)

def login(request):
    ctx = {}

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/partner/")

        else:
            ctx.update({ "error" : "존재하지 않는 사용자입니다." })


    return render(request, "login.html", ctx)

def logout(request):
    auth_logout(request)
    return redirect("/partner/")
