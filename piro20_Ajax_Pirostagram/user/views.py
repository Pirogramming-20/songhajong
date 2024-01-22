from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import User
from .forms import UserForm

def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('post:main')
    else:
        form = UserForm()
        ctx = {'form': form}
        return render(request, 'user/user_create.html', ctx)
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('post:main')
        return redirect('post:main')
    else:
        form = AuthenticationForm()
        ctx = {'form': form}
        return render(request, 'user/user_login.html', ctx)
    
def logout(request):
    auth.logout(request)
    return redirect('post:main')

