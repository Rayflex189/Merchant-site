from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('dash/', views.dash, name='dash'),
    path('bank/', views.bank, name='bank'),
    path('International_transfer/', views.International_transfer, name='International_transfer'),
    path('crypto/', views.crypto, name='crypto'),
    path('crypto_dp/', views.crypto_dp, name='crypto_dp'),
    path('crypto_wt/', views.crypto_wt, name='crypto_wt'),
    path('otp/', views.otp, name='otp'),
    path('imf/', views.imf, name='imf'),
    path('iban/', views.iban, name='iban'),
    path('paypal/', views.paypal, name='paypal'),
    path('pending/', views.pending, name='pending'),
    path('profile_edit/', views.UpdateProfile, name='profile_edit'),
    path('setting/', views.setting, name='setting'),
    path('analytics/', views.analytics, name='analytics'),
    path('terms/', views.terms, name='terms'),
    path('loan/', views.loan, name='loan'),
    path('loan_r/', views.loan_r, name='loan_r'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('verify/', views.verify, name='verify'),
    path('transfer/', views.transfer, name='transfer'),
    path('Deposit/', views.Deposit, name='Deposit'),
    path('transaction/', views.transaction, name='transaction'),
    path('logout/', views.LogoutPage, name='logout'),
    path('UpdateProfile/', views.UpdateProfile, name='UpdateProfile'),
]