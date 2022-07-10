from django.shortcuts import render
from django.contrib import messages
from .models import Account
from django.contrib.auth import (
                                  authenticate,
                                  logout ,
                                  login
                              )
from django.shortcuts import (
                                  render,
                                  get_object_or_404,
                                  redirect
                              )
from .forms import (
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateForm,
                )

def registration(request):
    """registration form"""
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            email = form.cleaned_data['email']
            raw_pass = form.cleaned_data['password1']
            account = authenticate(email=email, password = raw_pass)
            print(email, raw_pass)
            form.save()
            #login(request, account)
            messages.success(request, "You have been Registered as {}".format(request.user.username))
            return redirect('main:index')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
            
    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form
        return render(request, 'account/register.html', context)
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('main:index')

def login_view(request):
    """Renders Login Form"""
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('main:index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In')
            return redirect('main:index')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account(request):
    """Renders userprofile page"""
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors")
    else:
        form = AccountUpdateForm(initial={
            'email':request.user.email, 
            'username': request.user.username
        }
        )
    context['account_form'] = form
    return render(request, 'account/userprofile.html', context)