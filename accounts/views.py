from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, ForgotPasswordStep1Form, ForgotPasswordStep2Form

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('inventory:dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('inventory:dashboard')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('accounts:login')

def forgot_password_step1(request):
    if request.method == 'POST':
        form = ForgotPasswordStep1Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            request.session['reset_username'] = username
            return redirect('accounts:forgot_password_step2')
        else:
            messages.error(request, "This username does not exist.")
    else:
        form = ForgotPasswordStep1Form()
        
    return render(request, 'accounts/forgot_password_step1.html', {'form': form})

def forgot_password_step2(request):
    username = request.session.get('reset_username')
    if not username:
        return redirect('accounts:forgot_password_step1')
        
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('accounts:forgot_password_step1')
        
    if request.method == 'POST':
        form = ForgotPasswordStep2Form(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successful")
            del request.session['reset_username']
            # After success we expect the user to go to login. We will render step 2 with a success flag
            return render(request, 'accounts/forgot_password_step2.html', {'success': True})
    else:
        form = ForgotPasswordStep2Form()
        
    return render(request, 'accounts/forgot_password_step2.html', {'form': form, 'success': False})
