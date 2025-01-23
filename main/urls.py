from django.urls import path
from .views import index, get_balans, give_order, case_details, profile, balance_check, inventory_add, sell_item,  sell_all, reviews, gold, orders, 

urlpatterns = [
    path('index/', index, name= 'index'),
    path('balans_get/', get_balans, name='get_bakans'),
    path('give_order/', give_order, name='give_order'),
    path('case/<int:id>/', case_details, name='case_details'),
    path('profile/', profile, name='profile'),
    path('balance_check/', balance_check, name='balance_check'),
    path('inventory_add/', inventory_add, name='inventory'),
    path('sell_item/', sell_item, name='sell_item'),
    path('sell_all/', sell_all, name='sell_all'),
    path('reviews/', reviews, name='reviews'),
    path('gold/', gold, name='gold'),
    path('orders/', orders, name='orders'),

    
    path('balans_update/', update_balans, name='update_balans'),
]

