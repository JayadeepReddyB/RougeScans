from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    donation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('PENDING','Pending'),('COMPLETED','Completed')])
    razorpay_order_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Donation #{self.id} for {self.user.username}"
    
class DonationDetails(models.Model):
    donation = models.ForeignKey(Donation, related_name="donation_details", on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Detail for donation {self.donation.id}"
    
    
