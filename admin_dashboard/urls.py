from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blood_request/<int:pk>/edit/', views.edit_blood_request, name='edit_blood_request'),
    path('blood_request/<int:pk>/delete/', views.delete_blood_request, name='delete_blood_request'),
    path('user/<int:pk>/edit/', views.edit_user, name='edit_user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete_user'),
]
