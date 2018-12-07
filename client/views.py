from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from partner.models import Partner, Menu
from .models import Client, Order, OrderMenu

# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    category = request.GET.get("category")

    if not category:
        partner_list = Partner.objects.all()
    else:
        partner_list = Partner.objects.filter(category=category)

    category_list = set([
        (partner.category, partner.get_category_display())
        for partner in partner_list
    ])

    ctx = {
        "partner_list" : partner_list,
        "category_list" : category_list,
    }
    return render(request, "main.html", ctx)

def common_signup(request, ctx, group):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        target_group = Group.objects.get(name=group)
        user.groups.add(target_group)

        if group == "client":
            Client.objects.create(user=user, name=username)

            if group == "partner":
                return redirect("/partner/login/")
            else:
                return redirect("/login/")

    return render(request, "signup.html", ctx)

def signup(request):
    ctx = { "is_client" : True }
    return common_signup(request, ctx, "client")

def common_login(request, ctx, group):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if group not in [group.name for group in user.groups.all()]:
                ctx.update({ "error" : "접근 권한이 없습니다." })
            else:
                auth_login(request, user)
                next_value = request.GET.get("next")
                if next_value:
                    return redirect(next_value)
                else:
                    if group == "partner":
                        return redirect("/partner/")
                    else:
                        return redirect("/")

        else:
            ctx.update({ "error" : "존재하지 않는 사용자입니다." })

    return render(request, "login.html", ctx)

def login(request):
    ctx = { "is_client" : True }
    return common_login(request, ctx, "client")

def order(request, partner_id):
    ctx = {}
    # if request.user.is_anonymous:
    #     return redirect("/partner/login/")
    partner = Partner.objects.get(id=partner_id)
    menu_list = Menu.objects.filter(partner=partner)

    if request.method == "GET":
        ctx.update({
            "partner" : partner,
            "menu_list" : menu_list,
        })
    elif request.method == "POST":
        order = Order.objects.create(
            client=request.user.client,
            address="test",
        )
        for menu in menu_list:
            order_menu_count = request.POST.get(str(menu.id))
            order_menu_count = int(order_menu_count)
            if order_menu_count > 0:
                # order.order_menu.add(menu)
                order_item = OrderMenu.objects.create(
                    order=order,
                    menu=menu,
                    count=order_menu_count,
                )

    return render(request, "order_menu_list.html", ctx)
