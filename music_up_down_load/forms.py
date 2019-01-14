from django import forms
from .models import User1


class User1Form(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User1
        fields = ['Name', 'Surname', 'Username', 'Password', 'Email']