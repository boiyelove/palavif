from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.sites.models import Site
from model_utils.models import TimeStampedModel

# Create your models here.
User = settings.AUTH_USER_MODEL
GENDER_CHOICES =  (('male','male'), ('female', 'female'), ('transgender', 'transgender'), ('gender neutral', 'gender neutral'), ('non-binary', 'non-binary'), ('agender', 'agender'), ('pangender', 'pangender'), ('genderqueer','genderqueer'), ('two-spirit', 'two-spirit'), ('third gender', 'third gender'))

MARITAL_CHOICES = (('single','single',), ('married','married'),
	('widowed','widowed'), ('divorced','divorced'), ('separated','separated'),
	('registred partnership', 'registred partnership'))

class Profile(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	middle_name = models.CharField(max_length=60)
	sponsor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name = 'sponsor')
	referral = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='referral')
	country = CountryField()
	date_of_birth = models.DateField(null=True)
	is_root = models.BooleanField(default=False)
	phone_number = PhoneNumberField()
	gender = models.CharField(choices = GENDER_CHOICES, max_length=60, null=True)
	marital_status = models.CharField(choices = MARITAL_CHOICES, max_length=60, null=True)
	state_of_origin = models.CharField(max_length=60, null=True)
	occupation = models.CharField(max_length=60, null=True)

	def check_profile_completeness(self):
		if (self.sponsor and self.referral and self.phone_number) or self.is_root:
			return True
		return False

	def __str__(self):
		return "%(self.last_name)s  %(self.first_name)s"


class NextOfKinInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nexofkinInfo')
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	middle_name = models.CharField(max_length=60)
	relationship = models.CharField(max_length=60)


class ContactInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contactInfo')
	home_address = models.CharField(max_length=160, null=True, blank=True)
	country = CountryField()
	state_region = models.CharField(max_length=60, null=True, blank=True)
	city = models.CharField(max_length=60, null=True, blank=True)
	zip_code = models.CharField(max_length=6, null=True, blank=True)
	office_address = models.CharField(max_length=60, null=True, blank=True)

class ReligionInfo(TimeStampedModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='religionInfo')
	religion = models.CharField(max_length=60, null=True, blank=True)
	organization_name = models.CharField(max_length=60, null=True, blank=True)
	department_in_organization = models.CharField(max_length=60, null=True, blank=True)

class SiteProfile(TimeStampedModel):
	site = models.OneToOneField(Site, on_delete=models.CASCADE)


	class Meta:
		app_label = 'sites'


class Product(TimeStampedModel):
	title = models.CharField(max_length=60)
	price = models.PositiveIntegerField()



