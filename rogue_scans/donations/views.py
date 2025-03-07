from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages

from .models import Donation, DonationDetails
from .forms import DonationForm

@login_required
def create_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]  # Get validated amount
            # amount = form.save(commit=False)

            
            # Create the donation record
            donation = Donation.objects.create(
                user=request.user,
                amount= amount,  
                status="PENDING"
            )

             # Redirect to Razorpay payment processing
            return redirect('payment:create_razorpay_order', donation_id = donation.id)

        else:
            messages.error(request, "Invalid amount entered.")

    else:
        form = DonationForm()  # Show an empty form for GET request

    return render(request, "donation_form.html", {"form": form})


@login_required
def donation_history(request):
    """Display the donation history of the user."""
    donations = Donation.objects.filter(user=request.user).prefetch_related('donation_details').order_by('-donation_date')
    return render(request, 'donation_history.html', {'donations': donations})


@login_required
def cancel_donation(request, donation_id):
    """Cancel an donation and redirect the user."""
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)

    # Check if the donation is still pending
    if donation.status == "PENDING":
        donation.status = "CANCELLED"
        donation.save()
        messages.success(request, "Your donation has been cancelled.")
    else:
        messages.error(request, "This donation cannot be cancelled.")

    return redirect("homepage") 