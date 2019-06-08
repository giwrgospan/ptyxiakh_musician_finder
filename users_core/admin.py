from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Song, Lyrics
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import SignUpForm, UserUpdateForm

admin.site.register(Profile)
admin.site.register(Song)
admin.site.register(Lyrics)


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)




