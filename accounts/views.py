from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Profile

# Create your views here.
class AccountChecks:

	def dispatch(self, request, *args, **kwargs):
		try:
			if request.user.profile.check_profile_completeness():
				return HttpResponseRedirect(reverse_lazy('profile'))
		except Profile.DoesNotExist:
			return HttpResponseRedirect(reverse_lazy('register'))
		return super().dispatch(request, *args, **kwargs)



class CompleteRegistration(FormView):
	form_class = RegistrationForm
	template = 'forms.html'


class AccountSettings(TemplateView):
	template_name = 'account_settings.html'

class UserProfile(TemplateView):
	template_name = 'profile.html'

class Login(TemplateView):
	template_name = 'auth_login.html'

class Register(TemplateView):
	template_name = 'auth_register.html'

class Dashboard(LoginRequiredMixin, AccountChecks, TemplateView):
	template_name = 'dashboard.html'

class  Earnings(TemplateView):
	template_name = 'earnings.html'

class  Affliates(TemplateView):
	template_name = 'affliates.html'

class  Adverts(TemplateView):
	template_name = 'adverts.html'

class  BillPayment(TemplateView):
	template_name = 'bill_payment.html'
