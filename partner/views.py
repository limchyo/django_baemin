from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import PartnerForm, MenuForm
from .models import Menu

# Create your views here.
def index(request):
    ctx = {}
    if request.method == "GET":
        partner_form = PartnerForm()
        ctx.update({ "form" : partner_form })
    elif request.method == "POST":
        partner_form = PartnerForm(request.POST)
        if partner_form.is_valid():
            partner = partner_form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect("/partner/")
        else:
            ctx.update({ "form" : partner_form })


    return render(request, "index.html", ctx)

def signup(request):
    ctx = {}

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)

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

def edit_info(request):
    ctx = {}
    if request.method == "GET":
        # partner = Partner.objects.get(user=request.user)
        partner_form = PartnerForm(instance=request.user.partner)
        ctx.update({ "form" : partner_form })
    elif request.method == "POST":
        partner_form = PartnerForm(
            request.POST,
            instance=request.user.partner
        )
        if partner_form.is_valid():
            partner = partner_form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect("/partner/")
        else:
            ctx.update({ "form" : partner_form })

    return render(request, "edit_info.html", ctx)

def menu(request):
    ctx = {}

    menu_list = Menu.objects.filter(partner=request.user.partner)
    ctx.update({ "menu_list" : menu_list })

    return render(request, "menu_list.html", ctx)

def menu_add(request):
    ctx = {}
    if request.method == "GET":
        menu_form = MenuForm()
        ctx.update({ "form" : menu_form })
    elif request.method == "POST":
        menu_form = MenuForm(request.POST, request.FILES)
        if menu_form.is_valid():
            menu = menu_form.save(commit=False)
            menu.partner = request.user.partner
            menu.save()
            return redirect("/partner/menu/")
        else:
            ctx.update({ "form" : menu_form })

    return render(request, "menu_add.html", ctx)
