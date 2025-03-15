from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpUser, CreateProfile
from django.contrib import messages
from .models import User_Record
from django.core.paginator import Paginator
from django.db.models import Q

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
            return redirect('user_login')
    else:
        form = SignUpUser()
    
    return render(request, 'register.html', {'form': form})
        

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('user_login')
    
    records = User_Record.objects.all()
    paginator = Paginator(records, 3)

    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'records': records})

def search(request):
    term = request.GET.get('search', '')
    records = User_Record.objects.filter(Q (username__icontains=term))
    
    paginator = Paginator(records, 3)

    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'records': records})

def create_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add a profile")
        return redirect("user_login")
    
    form = CreateProfile(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'create_profile.html', {'form': form})
        
        