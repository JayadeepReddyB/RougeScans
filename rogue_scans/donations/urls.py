from django.urls import path
from . import views


urlpatterns = [
    # Route to create a new donation
    path('create/', views.create_donation, name='create_donation'),
    
    # Route to display the user's donation history
    path('donations/history/', views.donation_history, name='donation_history'),
    
    path('donation/cancel/<int:donation_id>', views.cancel_donation, name='cancel_donation')
]
