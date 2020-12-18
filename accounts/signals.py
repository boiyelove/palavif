from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *kwargs):
	if created:
		Profile.objects.create(user=instance)
