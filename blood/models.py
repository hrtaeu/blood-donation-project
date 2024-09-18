from django.db import models
from django.conf import settings

class BloodDonation(models.Model):
    DONATING = 'donating'
    LOOKING = 'looking'
    REQUEST_TYPE_CHOICES = [
        (DONATING, 'Donating'),
        (LOOKING, 'Looking'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    blood_type = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.request_type} request by {self.user}"
