from django.shortcuts import render
from partner.models import Partner
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

def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        return redirect("/partner/login/")
    ctx = { "is_client" : True }

    return render(request, "signup.html", ctx)

def login(request):
    ctx = { "is_client" : True }
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_value = request.GET.get("next")
            if next_value:
                return redirect(next_value)
            else:
                return redirect("/partner/")

        else:
            ctx.update({ "error" : "존재하지 않는 사용자입니다." })

    return render(request, "login.html", ctx)
