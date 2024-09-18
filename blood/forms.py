from django import forms
from .models import BloodDonation

class BloodDonationForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality', 'description']
