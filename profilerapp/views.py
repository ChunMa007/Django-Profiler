from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpUser, CreateProfile
from django.contrib import messages
from .models import User_Record
from django.core.paginator import Paginator
from django.db.models import Q

def getting_started(request):
    return render(request, 'getting_started.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('user_login')
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('user_login')

def user_register(request):
    if request.method == "POST":
        form = SignUpUser(request.POST)
        if form.is_valid():
            form.save()
            messages("User created successfully")
            return redirect('user_login')
    else:
        form = SignUpUser()
    
    return render(request, 'register.html', {'form': form})
        

def home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    term = request.GET.get('search', '')
    records_list = User_Record.objects.all().order_by('-id')

    if term:
        records_list = records_list.filter(Q(username__icontains=term))

    paginator = Paginator(records_list, 7)
    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)

    return render(request, 'home.html', {'records': records, 'term': term})

def create_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add a profile")
        return redirect("user_login")
    
    form = CreateProfile(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Profile created successfully")
            return redirect('home')
    
    return render(request, 'create_profile.html', {'form': form})
        
def view_profile(request, username):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('user_login')

    current_record = User_Record.objects.get(username=username)
    form = CreateProfile(instance=current_record)
    
    if 'image' in form.fields:
        del form.fields['image']

    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True
    
    return render(request, 'view_profile.html', {'form': form, 'current_record': current_record})

def edit_profile(request, username):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('user_login')

    current_record = User_Record.objects.get(username=username)
    form = CreateProfile(request.POST or None, request.FILES or None, instance=current_record)
    
    if request.method == "POST":    
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
    return render(request, 'edit_profile.html', {'form': form, 'current_record': current_record})

def delete_profile(request, username):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in")
        return redirect('user_login')
    
    delete_record = get_object_or_404(User_Record, username=username)
    delete_record.delete()
    messages.error(request, "User deleted successfully")
    return redirect('home')