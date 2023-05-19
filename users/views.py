from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from .models import UsersAb
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView


class RegisterUser(CreateView):
    model = User
    template_name = "authorizate/register.html"
    form_class = RegisterForm
    
    
    def get_success_url(self) -> str:
        return reverse('home')


# #class LoginView(FormView):
#     model = UsersAb
#     template_name = "home.html"
#     form_class = LoginForm

#     def get_success_url(self) -> str:
#         return reverse('list')


class LoginView(TemplateView):
    model = UsersAb
    template_name = "authorizate/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
        message = 'Notogri Username yoki Parol!'
        return render(request, self.template_name, context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect("home")


