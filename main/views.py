
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, ListView
from users.models import UsersAb
from django.contrib.auth.models import User
from .forms import Update_balanseFORM
from main.my_func import gold_com
from users.forms import ImageChangeForm, ProfileChangeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



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
    case = Cases.objects.get(id=id)
    case_items = case.items.all().order_by("chance")
    context = {
        "case": case,
        "cases_items": case_items
    }
    return render(request, 'case_details.html', context)

@csrf_exempt
def balance_check(request):
    if request.POST:
        user_sum = UsersAb.objects.get(id=request.user.id).sum
        case_price = request.POST.get("case_price")
        sum = float(user_sum)-float(case_price)
        UsersAb.objects.filter(id=request.user.id).update(sum=sum)
        return HttpResponse("Ok")
    user_id = request.user.id
    balance_sum = UsersAb.objects.get(id=user_id).sum
    return JsonResponse({"sum":balance_sum})
    


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
    user_profile = UsersAb.objects.get(id = request.user.id)
    user_profile1 = UsersAb.objects.filter(id = request.user.id)
    print(request.FILES)

    if request.POST and request.FILES:
            image_form = ImageChangeForm(request.POST, request.FILES, instance=user_profile)
            if image_form.is_valid():
                # img =image_form.cleaned_data['image']
                # print(img)
                # user_profile1.update(image=img)
                image_form.save()
                return redirect('profile')

    elif request.POST:
        profile_form = ProfileChangeForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')              
    
    context = {
        'img_change': ImageChangeForm,
        'profile_change': ProfileChangeForm
    }
    return render(request, 'Users/profile.html', context)
    




