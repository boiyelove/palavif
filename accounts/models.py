from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.sites.models import Site
from model_utils.models import TimeStampedModel

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	sponsor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name = 'sponsor')
	referral = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='referral')
	country = CountryField()
	is_root = models.BooleanField(default=False)
	phone_number = PhoneNumberField()

	def check_profile_completeness(self):
		if (self.sponsor and self.referral and self.phone_number) or self.is_root:
			return True
		return False

	def __str__(self):
		return "%(self.last_name)s  %(self.first_name)s"



class SiteProfile(TimeStampedModel):
	site = models.OneToOneField(Site, on_delete=models.CASCADE)


	class Meta:
		app_label = 'sites'


class Product(TimeStampedModel):
	title = models.CharField(max_length=60)
	price = models.PositiveIntegerField()



