from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as Sfm



User = get_user_model()


class RegistrationForm:

	def clean_phone_number(self):
		phone_number = self.cleaned_data['phone_number']
		if Profile.objects.filter(phone_number=phone_number).exists():
			raise forms.ValidationError('Sorry, user with phone number already exists')
		return phone_number

	def clean_sponsor(self):
		sponsor = self.cleaned_data['sponsor']
		if sponsor.strip() and User.objects.filter(username=sponsor).exists():
			raise  forms.ValidationError('Enter a valid sponsor')
		return sponsor


	# def clean_referral(self):
	# 	referral = self.cleaned_data['referral']
	# 	if sponsor.trim() and User.objects.filter(username=referral).exists():
	# 		raise forms.ValidationError('Sorry, user with this referral code does not exist.')
	# 	return referral

	# def signup(self, request, user):

	def save(self, request):
		user = super(SocialSignupForm, self).save(request)
		#other process
		return user

class SignupForm(SignupForm):
	sponsor = forms.CharField(required=False)
	first_name = forms.CharField()
	last_name = forms.CharField()
	terms = forms.BooleanField(initial=True)

	def save(self, request):
		user = super(SignupForm, self).save(request)
		
		try:
			sponsor = User.objects.get(username = self.cleaned_data.get('sponsor', None))
		except User.DoesNotExist:
			sponsor = None
		try:
			referral = User.objects.get(username = request.session.get('referral', None))
		except User.DoesNotExist:
			referral =  None
			
		Profile.objects.create(user=user,
			sponsor = sponsor,
			referral = referral,
			first_name = self.cleaned_data.get('first_name'),
			last_name = self.cleaned_data.get('last_name'))
		return user

	def clean_sponsor(self):
		sponsor = self.cleaned_data['sponsor']
		if sponsor.strip() and not User.objects.filter(username=sponsor).exists():
			raise  forms.ValidationError('Enter a valid sponsor')
		return sponsor

class SocialSignupForm(RegistrationForm, Sfm):
	class Meta:
		model = Profile
		fields = ('sponsor', 'referral', 'country', 'phone_number')


