# account/urls.py

from django.urls import path
from .views import register, login, create_profile, home, ProfileUpdateView, profile_view
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create-profile/', create_profile, name='create_profile'),
    path('', home, name='home'),  # Ensure home is available at the root
    path('profile/', profile_view, name='profile_view'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
