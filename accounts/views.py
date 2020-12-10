from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AccountSettings(TemplateView):
	template_name = 'account_settings.html'
class UserProfile(TemplateView):
	template_name = 'profile.html'
class Login(TemplateView):
	template_name = 'auth_login.html'
class Register(TemplateView):
	template_name = 'auth_register.html'
