from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, ModelForm, Form
from .models import UsersAb



class ProfileChangeForm(ModelForm):
    first_name = forms.CharField(required=False, widget=forms.widgets.Input(attrs={"class":"user__btn modal-input", "placeholder":"Ism"}))
    last_name = forms.CharField(required=False, widget=forms.widgets.Input(attrs={"class":"user__btn modal-input", "placeholder":"Familiya"}))
    number = forms.IntegerField(required=False, widget=forms.widgets.Input(attrs={"class":"user__btn modal-input", "placeholder":"Number"}))
    tg = forms.CharField(required=False, widget=forms.widgets.Input(attrs={"class":"user__btn modal-input", "placeholder":"Telegram Username"}))

    class Meta:
        model = UsersAb
        fields = [
            "first_name",
            'last_name',
            'number',
            'tg'
        ]


class ImageChangeForm(ModelForm):
    image = forms.ImageField(required=False, widget=forms.widgets.FileInput(attrs={"type":"file", "name":"file", "id":"file111"}), label="")

    class Meta:
        model = UsersAb
        fields = [
            'image'
        ]

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
