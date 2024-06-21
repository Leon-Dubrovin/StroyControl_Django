from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User, Predpisania
from django.shortcuts import render
from .forms import LoginForm,UserForm
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    loginform = LoginForm()
    return render(request, "main_page.html", {"form":loginform})

def about(request):
    loginform = LoginForm()
    return render(request, "about.html", {"form":loginform})

def SK(request):
    loginform = LoginForm()
    return render(request, "SK.html", {"form":loginform})

def TKzaII(request):
    loginform = LoginForm()
    return render(request, "TKzaII.html", {"form":loginform})

def DK(request):
    loginform = LoginForm()
    return render(request, "DK.html", {"form":loginform})

def techzakaz(request):
    loginform = LoginForm()
    return render(request, "techzakaz.html", {"form":loginform})

def TA(request):
    loginform = LoginForm()
    return render(request, "TA.html", {"form":loginform})

def contacts(request):
    loginform = LoginForm()
    return render(request, "contacts.html", {"form":loginform})

def prov(request):
    if request.method == "POST":
        loginn = request.POST.get("login")
        password = request.POST.get("password")
        try:
            user = User.objects.get(first_name=loginn, password=password)
            return HttpResponseRedirect(f"/reg_predp/{user.id}")
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/")

def reg_predp(request,id):
    user = User.objects.get(id=id)
    predpisania = Predpisania.objects.all()

    return render(request, "reg_predp.html", {"predpisania": predpisania, "user": user})

def kab(request,id):
    user = User.objects.get(id=id)
    return render(request, "kab.html", {"user": user})

def filter_zakazchik(request,id):
    Zakazchik = request.POST.get("Zakazchik")
    user = User.objects.get(id=id)
    predpisania = Predpisania.objects.filter(Zakazchik__icontains=Zakazchik)
    return render(request, "reg_predp.html", {"predpisania": predpisania, "user": user})

def filter_podryadchik(request,id):
    Podryadchik = request.POST.get("Podryadchik")
    user = User.objects.get(id=id)
    predpisania = Predpisania.objects.filter(Podryadchik__icontains=Podryadchik)
    return render(request, "reg_predp.html", {"predpisania": predpisania, "user": user})

def filter_predp_date(request,id):
    predp_date = request.POST.get("predp_date")
    user = User.objects.get(id=id)
    predpisania = Predpisania.objects.filter(predp_date__lte = predp_date)
    return render(request, "reg_predp.html", {"predpisania": predpisania, "user": user})

def reg(request):
    userform = UserForm()
    return render(request, "reg.html", {"form": userform})

def create_user(request):
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.password = request.POST.get("password")
        user.email = request.POST.get("email")
        user.age = request.POST.get("age")
        user.save()
    return HttpResponseRedirect(f"/reg_predp/{user.id}")