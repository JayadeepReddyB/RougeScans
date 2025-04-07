from django import forms
from .models import Donation
from django.forms import ModelForm,NumberInput

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            "amount"
        ]

        widgets = {
            'amount' : forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width:400px',
                'placeholder': 'Donation',
                'min': 1,
                'max': 100000,
                'step': 1
            })
        }

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount is None:
            raise forms.ValidationError("Amount is required.")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")

        if amount > 100000:
           raise forms.ValidationError("Amount exceeds the maximum limit.")

        return amount
    

