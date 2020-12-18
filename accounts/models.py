from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	sponsor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name = 'sponsor')
	referral = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='referral')
	country = CountryField()
	is_root = models.BooleanField(default=False)
	phone_number = PhoneNumberField()

	def check_profile_completeness(self):
		if (self.sponsor and self.referral and self.phone_number) or self.is_root:
			return True
		return False

