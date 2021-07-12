from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
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
