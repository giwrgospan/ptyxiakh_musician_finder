# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('Name', 'Surname', 'Mail_or_Phone', 'Username', 'Password', 'Date_of_Birth')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('Name', 'Surname', 'Mail_or_Phone', 'Username', 'Password', 'Date_of_Birth')