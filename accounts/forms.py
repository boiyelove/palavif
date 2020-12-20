from django import forms
from .models import Profile
from django.conf import settings
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as Sfm
User = settings.AUTH_USER_MODEL


class RegistrationForm:
	class Meta:
		model = Profile
		fields = ('sponsor', 'referral', 'country', 'phone_number')

	def clean_phone_number(self):
		phone_number = self.cleaned_data['phone_number']
		if Profile.objects.filter(phone_number=phone_number).exists():
			raise forms.ValidationError('Sorry, user with phone number already exists')
		return phone_number

	def clean_sponsor(self):
		sponsor = self.cleaned_data['sponsor']
		if sponsor.trim() and User.objects.filter(username=sponsor).exists():
			raise  forms.ValidationError('Enter a valid sponsor')
		return sponsor


	def clean_referral(self):
		referral = self.cleaned_data['referral']
		if sponsor.trim() and User.objects.filter(username=referral).exists():
			raise forms.ValidationError('Sorry, user with this referral code does not exist.')
		return referral

	def save(self, request):
		user = super(SocialSignupForm, self).save(request)
		#other process
		return user

class SignupForm(RegisterationForm, Sfm):
	pass

class SocialSignupForm(RegisterationForm, Sfm):
	pass

