from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Just Logged In'))
            return redirect('index')
        else:
            messages.success(request, ('Error Logging You In'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    messages.success(request, ('You Just Logged Out'))
    logout(request)
    return redirect('index')