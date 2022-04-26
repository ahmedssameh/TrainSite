from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def Update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('index')
    else:

        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form': u_form}
    return render(request, 'user/Update.html', context)


def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            htmly = get_template('user/Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            txt = EmailMultiAlternatives(subject, html_content, from_email, [to])
            txt.attach_alternative(html_content, "text/html")
            txt.send()

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('user/login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'reqister here'})



def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)

            #messages.success(request, f' wecome {username} !!')
            return redirect('http://127.0.0.1:8000/home/mainpage')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})