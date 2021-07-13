from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == "POST":
        logform = LoginForm(request.POST)
        if logform.is_valid():
            logdata = logform.cleaned_data
            user = authenticate(request,
                                username=logdata['username'],
                                password=logdata['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticate successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        logform = LoginForm()
    return render(request,
                  'account/signin.html',
                  {'form': logform})

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': dashboard})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request,
                  'account/register.html',
                  {'form': user_form})