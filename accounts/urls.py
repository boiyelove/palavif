from django.urls import path
from . import views

urlpatterns = [

	path('account_settings/', views.AccountSettings.as_view(), name='account-settings'),
	path('profile/', views.UserProfile.as_view(), name='account-profile'),
]