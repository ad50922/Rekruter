from django.urls import path
from . import views

app_name = 'RekruterApp'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("oferty-pracy", views.oferty, name="oferty-pracy"),
    path("dodaj", views.dodaj_oferte, name="dodaj"),
]
