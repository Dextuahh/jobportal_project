from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Don't log the user in automatically — require explicit login
            messages.success(request, 'Registration successful. Please log in.')
            # Respect 'next' parameter by forwarding it to the login page
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(f"/auth/login/?next={next_url}")
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserRegistrationForm()
    # pass a safe `next` value into the template so templates don't try to access QueryDict keys
    next_param = request.GET.get('next') or request.POST.get('next')
    return render(request, 'security/register.html', {'form': form, 'next': next_param})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                # If a next parameter was provided, redirect there. Otherwise go to the jobs list.
                next_url = request.GET.get('next') or request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('jobs:job_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    # pass `next` into the template context for the hidden field and re-renders
    next_param = request.GET.get('next') or request.POST.get('next')
    return render(request, 'security/login.html', {'form': form, 'next': next_param})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
