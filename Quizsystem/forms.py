from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class studForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    school_name=forms.CharField(max_length=100)
    std=forms.IntegerField()

class teachForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email' ,'password')
    school_name = forms.CharField(max_length=100)
    std = forms.IntegerField()
