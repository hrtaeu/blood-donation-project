# blood_donation_project/urls.py

from django.contrib import admin
from django.urls import path, include



import blood
from account.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', home, name='home'),  # Include account app URLs
    path('blood/', include('blood.urls')),
    path('dashboard/', include('admin_dashboard.urls')),
    ]
