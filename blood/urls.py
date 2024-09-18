# blood/urls.py
from django.urls import path
from .views import (
    BloodDonationCreateView,
    BloodDonationUpdateView,
    BloodDonationDeleteView,
    BloodDonationListView,
    BloodDonationDetailView
)

urlpatterns = [
    path('create/', BloodDonationCreateView.as_view(), name='create_blood_donation'),
    path('<int:pk>/update/', BloodDonationUpdateView.as_view(), name='update_blood_donation'),
    path('<int:pk>/delete/', BloodDonationDeleteView.as_view(), name='delete_blood_donation'),
    path('', BloodDonationListView.as_view(), name='blood_donation_list'),
    path('<int:pk>/', BloodDonationDetailView.as_view(), name='blood_donation_detail'),
]
