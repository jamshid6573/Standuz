from django.urls import path
from .views import RegisterUser, LoginView, logout_user

urlpatterns = [
    path("", LoginView.as_view(), name="home"),
    path("registrations/", RegisterUser.as_view(), name="register"),
    path("logout/", logout_user, name="logout")
]

