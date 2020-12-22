from django.urls import path
from . import views

urlpatterns = [

	path('account_settings/', views.AccountSettings.as_view(), name='account-settings'),
	path('', views.Login.as_view(), name='login'),
	path('register/', views.Register.as_view(), name='register'),
	path('dashboard/',views.Dashboard.as_view(), name='dashboard'),


	path('earnings/', views.Earnings.as_view(), name='earnings'),
	path('affliates/', views.Affliates.as_view(), name='affliates'),
	path('adverts/', views.Adverts.as_view(), name='adverts'),
	path('bill_payment/', views.BillPayment.as_view(), name='bill-payment'),

]