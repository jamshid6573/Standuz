
from email.mime import image
from django import forms
from django.forms import NumberInput, Form, ModelForm

class Update_balanseFORM(Form):
    gold = forms.CharField(widget=NumberInput(), required=False)

