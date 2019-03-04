from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

YEARS = [x for x in range(1940, 2019)]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Όνομα')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label='Επίθετο')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Ημερομηνία Γένννησης')
    password1 = forms.CharField( label='Κωδικός Πρόσβασης', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Επιβεβαίωση Κωδικού Πρόσβασης', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date')
        labels = {'username': "Όνομα Χρήστη", }


