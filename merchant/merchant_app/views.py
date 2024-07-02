from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.db import IntegrityError
from .decorators import *
from .models import *


# Create your views here.


def home(request):
    return render(request, 'merchant_app/index.html')

@login_required(login_url='loginpage')
def UpdateProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dash')  # Redirect to the same page after successful update
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'form': form
    }
    return render(request, 'merchant_app/profile_edit.html', context)

@unauthenticated_user
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('UpdateProfile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'merchant_app/login.html')

@login_required(login_url='loginpage')
def dash(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/dashboard.html', context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'merchant_app/register.html', context)

@login_required(login_url='loginpage')
def bank(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'merchant_app/bank.html', context)

@login_required(login_url='loginpage')
def International_transfer(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'merchant_app/it.html', context)

@login_required(login_url='loginpage')
def crypto_dp(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'merchant_app/crypto_dp.html', context)

@login_required(login_url='loginpage')
def crypto_wt(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'merchant_app/crypto_wt.html', context)

@login_required(login_url='loginpage')
def crypto(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'merchant_app/crypto.html', context)


@login_required(login_url='loginpage')
def otp(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/otp.html', context)

@login_required(login_url='loginpage')
def imf(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/imf.html', context)

@login_required(login_url='loginpage')
def loan(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/loan.html', context)

@login_required(login_url='loginpage')
def loan_r(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/loan_r.html', context)

@login_required(login_url='loginpage')
def coming_soon(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/coming_soon.html', context)


@login_required(login_url='loginpage')
def verify(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/verify.html', context)

@login_required(login_url='loginpage')
def iban(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/iban.html', context)

@login_required(login_url='loginpage')
def paypal(request):
    user_profile = request.user.userprofile  # Retrieve user profile associated with current user

    if request.method == 'POST':
        form = DepositForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('otp')  # Replace 'dashboard' with your actual dashboard URL name
            except ValidationError as e:
                form.add_error(None, str(e))  # Add non-field error for insufficient funds
    else:
        form = DepositForm(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'merchant_app/paypal.html', context)

@login_required(login_url='loginpage')
def pending(request):
    return render(request, 'merchant_app/pending.html')

def reset(request):
    return render(request, 'merchant_app/reset.html')

@login_required(login_url='loginpage')
def setting(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dash')  # Redirect to the same page after successful update
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile,  'form': form}
    return render(request, 'merchant_app/setting.html', context)


def terms(request):
    return render(request, 'merchant_app/terms.html')

@login_required(login_url='loginpage')
def transfer(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/transfer.html', context)

@login_required(login_url='loginpage')
def Deposit(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/deposit.html', context)


@login_required(login_url='loginpage')
def transaction(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/transaction.html', context)

@login_required(login_url='loginpage')
def analytics(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        # You can create a new UserProfile or redirect to a different page
        user_profile = UserProfile.objects.create(user=request.user)
    balance = user_profile.balance
    context = {'user_profile':user_profile}
    return render(request, 'merchant_app/analytics.html', context)

@login_required(login_url='loginpage')
def LogoutPage(request):
    logout(request)
    return redirect('loginpage')
