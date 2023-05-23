from django.urls import path
from .views import index, get_balans, give_order, case_details, profile

urlpatterns = [
    path('index/', index, name= 'index'),
    path('balans_get/', get_balans, name='get_bakans'),
    path('give_order/', give_order, name='give_order'),
    path('case/<int:id>/', case_details, name='case_details'),
    path('profile/', profile, name='profile'),
    
    #path('balans_update/', update_balans, name='update_balans'),
]

