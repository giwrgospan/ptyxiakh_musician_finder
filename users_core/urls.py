
from django.urls import path

# Από τον current directory βρές το αρχείο views και κάντο import
from . import views

app_name = 'users_core'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

]