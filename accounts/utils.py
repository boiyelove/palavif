from .models import Profile

def find_incomplete_downline(profile):
	num = Profile.objects.filter(sponsor=profile.user).count()
	if num < 3:
		pass
	return profile