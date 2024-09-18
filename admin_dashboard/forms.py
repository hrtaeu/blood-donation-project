from django import forms
from blood.models import BloodDonation
from django.contrib.auth.forms import UserChangeForm

class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality', 'description']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
