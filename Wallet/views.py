
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from .forms import WalletUpdateForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = WalletUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            WalletId = form.cleaned_data.get('WalletId')
            email = form.cleaned_data.get('email')

            d = {'WalletId': WalletId}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('http://127.0.0.1:8000/seatstrain/seats')
    else:
        form = WalletUpdateForm()
    return render(request, 'Wallet/Wallet.html', {'form': form, 'title': 'reqister here'})



def log(request):

    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__
        #WalletId = request.POST['WalletId']
        #Password = request.POST['Password']
        WalletId = request.POST.get('WalletId')
        Password = request.POST.get('Password')
        Wallet = authenticate(request, WalletId=WalletId, Password=Password)
        print(request.POST)
        if Wallet is not None:
            P_form = login(request, Wallet)

            #messages.success(request, f' wecome {username} !!')
            return redirect('http://127.0.0.1:8000/home/mainpage')
        else:
            messages.info(request, f'Wallet does not exist')
    P_form = AuthenticationForm()

    return render(request, 'Wallet/acceptPayment.html', {'P_form': P_form, 'title': 'acceptPayment'})