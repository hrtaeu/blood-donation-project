from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            auth_login(request, user)
            return redirect('home')  # Redirect to homepage or another page
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')  # Redirect to homepage or another page after logout

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Check if the user has a profile
            if UserProfile.objects.filter(user=user).exists():
                auth_login(request, user)
                return redirect('home')  # Redirect to home if profile exists
            else:
                # Redirect to profile creation form if no profile exists
                return redirect('create_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')  # Redirect to home after profile creation
    else:
        form = UserProfileForm()
    return render(request, 'account/create_profile.html', {'form': form})

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'account/profile.html', {'user_profile': user_profile})

def home(request):
    return render(request, 'home.html')

class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'availability']
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('profile')  # Redirect after successful update

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)

    def form_valid(self, form):
        # Check if blood_type is being changed
        if 'blood_type' in form.changed_data:
            form.add_error('blood_type', 'Blood type cannot be changed.')
            return self.form_invalid(form)

        profile = form.instance
        if profile.availability and profile.last_donation_date:
            days_since_last_donation = (timezone.now().date() - profile.last_donation_date).days
            if days_since_last_donation < 56:
                form.add_error('availability',
                               f'You must wait {56 - days_since_last_donation} more days before changing availability.')
                return self.form_invalid(form)

        return super().form_valid(form)
