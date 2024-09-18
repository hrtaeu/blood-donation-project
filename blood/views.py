from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BloodDonation
from .forms import BloodDonationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

class BloodDonationCreateView(LoginRequiredMixin, CreateView):
    model = BloodDonation
    form_class = BloodDonationForm
    template_name = 'blood/blood_donation_form.html'

    def form_valid(self, form):
        # Auto-fill fields based on profile if the request type is 'donating'
        if form.cleaned_data['request_type'] == BloodDonation.DONATING:
            profile = self.request.user.userprofile
            form.instance.blood_type = profile.blood_type
            form.instance.region = profile.region
            form.instance.province = profile.province
            form.instance.municipality = profile.municipality
        return super().form_valid(form)

class BloodDonationUpdateView(LoginRequiredMixin, UpdateView):
    model = BloodDonation
    form_class = BloodDonationForm
    template_name = 'blood/blood_donation_form.html'

    def get_queryset(self):
        # Allow only the user to update their own requests
        return BloodDonation.objects.filter(user=self.request.user)

class BloodDonationDeleteView(LoginRequiredMixin, DeleteView):
    model = BloodDonation
    success_url = reverse_lazy('blood_donation_list')

    def get_queryset(self):
        # Allow only the user to delete their own requests
        return BloodDonation.objects.filter(user=self.request.user)

class BloodDonationListView(LoginRequiredMixin, ListView):
    model = BloodDonation
    template_name = 'blood/blood_donation_list.html'
    context_object_name = 'donations'

    def get_queryset(self):
        return BloodDonation.objects.all()

class BloodDonationDetailView(LoginRequiredMixin, DetailView):
    model = BloodDonation
    template_name = 'blood/blood_donation_detail.html'

