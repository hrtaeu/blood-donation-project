# account/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality',
                          'blood_type', 'availability']
