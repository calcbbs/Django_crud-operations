from django import forms
from django.core import validators
from logicapp.models import *


class AdminLogin(forms.Form):
    Login_ID = forms.CharField()
    Password = forms.CharField()
class AddLeads(forms.ModelForm):

    Course_Fee = forms.IntegerField()

    Aggregate = forms.IntegerField()

    class Meta():
        model = AddLeads
        fields="__all__"
