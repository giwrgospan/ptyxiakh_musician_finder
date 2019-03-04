
from django.urls import path

# Από τον current directory(music_up_down_load) βρές το αρχείο views και κάντο import
from . import views

app_name = 'users_core'

urlpatterns = [
    path('', views.signup, name='signup'),
]