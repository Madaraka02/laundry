from django.db import models

# Create your models here.
PAYMENT_CHOICES = (
    ("CASH", "CASH"),
    ("MPESA", "MPESA"),
    ("SWIPE", "SWIPE"),
)

CONDITION_CHOICES = (
    ("GOOD", "GOOD"),
    ("BAD", "BAD"),
)


class Client(models.Model):
    client_name = models.CharField(max_length=400, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_in_time = models.TimeField(null=True, blank=True)
    picked = models.BooleanField(default=False)
    check_out_date = models.DateTimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    payment_method = models.CharField(max_length = 20,choices = PAYMENT_CHOICES, default = 'CASH')    
