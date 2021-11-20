from django import forms
from django.contrib.auth.models import User
from second_app.models import UserProfileInfoForm

class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoForm
        fields =('portfolio_sites','profile_pic')