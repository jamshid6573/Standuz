from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, ModelForm
from .models import UsersAb


class RegisterForm(UserCreationForm, ModelForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        error_messages={"mes": "notogri"},
        widget=forms.PasswordInput(attrs={"autocomplete": 'new-password', "placeholder": 'Parol', "class": 'log'}),  
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": 'new-password', "placeholder": 'Parolni takrorlang', "class": 'log'}),
        strip=False,
        error_messages={"mes": "notogri"}
    )

    class Meta:
        model = UsersAb
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

        widgets = {
             'username':forms.TextInput(attrs={"placeholder": 'Username', "class": 'log' }),
             'email':forms.EmailInput(attrs={"placeholder": 'Email', "class": 'log'}),
        }


        # labels = {
        # }


# class LoginForm(AuthenticationForm):
#     class Meta:
#         fields = '__all__'

class LoginForm(forms.Form):
    username = CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": 'Login', "class": 'log' }))
    password = CharField(max_length=255, widget=forms.PasswordInput(attrs={"placeholder": 'Parol', "class": 'log' }))
