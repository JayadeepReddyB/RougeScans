from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            "amount"
        ]

        def clean_Amount(self):
            """Ensure donation amount is positive."""
            amount = self.cleaned_data.get("Amount")
            if amount <= 0:
                raise forms.ValidationError("Donation amount must be greater than zero.")
            return amount
    

