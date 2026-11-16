from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StaffLoginForm

def staff_login_view(request):
    """
    Staff and Librarian login view.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:overview')

    if request.method == 'POST':
        form = StaffLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.get_full_name() or user.username}!")
            next_url = request.GET.get('next') or 'dashboard:overview'
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please verify your staff credentials.")
    else:
        form = StaffLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def staff_logout_view(request):
    """
    Staff logout view.
    """
    logout(request)
    messages.info(request, "You have been logged out safely.")
    return redirect('core:home')


@login_required
def staff_profile_view(request):
    """
    Display logged-in staff member profile and details.
    """
    return render(request, 'accounts/profile.html', {'user': request.user})

