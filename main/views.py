
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, ListView
from users.models import UsersAb
from django.contrib.auth.models import User
from .forms import Update_balanseFORM
from main.my_func import gold_com

def index(request):
    if request.user.is_authenticated:
        context = {
            'skin': Skins.objects.get(skin="Akr Necromanser"),
            'Cases': Cases.objects.all()
        }
        return render(request, 'gold.html', context)
    else:
        return redirect('home')

def case_details(request, id):
    return render(request, 'case_details.html')


def get_balans(request):
    context = {}
    if request.POST:
        id = request.POST.get("id")
        update_gold = request.POST.get("gold")
        print(update_gold)
        try:
            user = UsersAb.objects.get(id=str(id))
            context["id"] = user.id
            context["name"] = user.username
            context["gold"] = user.gold

            if update_gold:
                gold = float(user.gold) + float(update_gold)
                UsersAb.objects.filter(id=id).update(gold=gold)



            

            return render(request, "admin/balanse_update.html", context)

        except:
            return render(request, "admin/balanse_update.html", {"error":"Topilmadi"})
    return render(request, "admin/balanse_update.html")

def give_order(request):
    skin =  skin = Skins.objects.get(skin="Akr Necromanser")
    if request.POST:
        if request.POST.get("click") == 'CHIQAZISH':
            gold = request.POST.get('gold')
            gold_commision = gold_com(float(gold))
            print(gold_commision)

    
    return render(request, "gold.html")

def profile(request):
    return render(request, 'Users/profile.html')
    




