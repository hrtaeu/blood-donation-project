from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserChangeForm
from blood.models import BloodDonation  # Correct model import
from blood.forms import BloodDonationForm  # Ensure this is the correct form
from account.models import CustomUser

# Check if user is admin
def admin_required(function=None):
    return user_passes_test(lambda u: u.is_superuser, login_url='login')(function)

@login_required
@admin_required
def dashboard(request):
    blood_requests = BloodDonation.objects.all()  # Fetch all blood donation requests
    users = CustomUser.objects.all()  # Fetch all users
    return render(request, 'admin_dashboard/dashboard.html', {
        'blood_requests': blood_requests,
        'users': users
    })

@login_required
@admin_required
def edit_blood_request(request, pk):
    blood_request = get_object_or_404(BloodDonation, pk=pk)  # Fetch blood donation request by primary key
    if request.method == 'POST':
        form = BloodDonationForm(request.POST, instance=blood_request)  # Use BloodDonationForm
        if form.is_valid():
            form.save()  # Save the updated blood donation request
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = BloodDonationForm(instance=blood_request)  # Initialize form with existing data
    return render(request, 'admin_dashboard/edit_blood_request.html', {'form': form})

@login_required
@admin_required
def delete_blood_request(request, pk):
    blood_request = get_object_or_404(BloodDonation, pk=pk)  # Fetch blood donation request by primary key
    if request.method == 'POST':
        blood_request.delete()  # Delete the blood donation request
        return redirect('dashboard')  # Redirect to the dashboard after deletion
    return render(request, 'admin_dashboard/delete_blood_request.html', {'blood_request': blood_request})

@login_required
@admin_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # Fetch user by primary key
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)  # Initialize form with existing user data
        if form.is_valid():
            form.save()  # Save the updated user details
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = UserChangeForm(instance=user)  # Initialize form with existing data
    return render(request, 'admin_dashboard/edit_user.html', {'form': form})

@login_required
@admin_required
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # Fetch user by primary key
    if request.method == 'POST':
        user.delete()  # Delete the user
        return redirect('dashboard')  # Redirect to the dashboard after deletion
    return render(request, 'admin_dashboard/delete_user.html', {'user': user})
