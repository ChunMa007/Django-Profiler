from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpUser
from django.contrib import messages

def getting_started(request):
    return render(request, 'getting_started.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('user_login')
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_register(request):
    if request.method == "POST":
        form = SignUpUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect('user_login')
    else:
        form = SignUpUser()
    
    return render(request, 'register.html', {'form': form})
        

def home(request):
    return render(request, 'home.html', {})
        
        