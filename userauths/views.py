# userauths/views.py
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth import login, authenticate, logout  # type: ignore
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm

def register_view(request):
    # Cek apakah user sudah login
    if request.user.is_authenticated:
        return redirect('index')  # Arahkan ke halaman 'index' jika sudah login
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Pastikan 'index' adalah URL tujuan yang valid
    else:
        form = UserRegisterForm()
    
    return render(request, 'userauths/sign-up.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # redirect ke halaman home jika user sudah login
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username atau password salah')
    else:
        form = UserLoginForm()
    
    return render(request, 'userauths/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # ganti 'login' dengan URL halaman login Anda

@login_required(login_url='login')
def home_view(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')