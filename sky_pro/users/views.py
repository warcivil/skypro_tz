from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/home/products/'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm


class CustomLogoutView(LogoutView):
    next_page = '/users/login/'
