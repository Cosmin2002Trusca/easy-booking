from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from .models import Booking, Table
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

# Booking

@login_required
def create_booking(request):
    class InlineBookingForm(forms.ModelForm):
        class Meta:
            model = Booking
            fields = [
                'customer_name', 'customer_email', 'customer_phone',
                'table', 'booking_date', 'booking_time', 
                'number_of_guests', 'special_request'
            ]

    if request.method == 'POST':
        form = InlineBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home or success page
    else:
        form = InlineBookingForm()

    return render(request, 'easy_booking/reservation_form.html', {'form': form})

# Authentification

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            login(request, user)  # Log in the user immediately
            return redirect('create_booking')  # Redirect to booking page
    else:
        form = UserCreationForm()

    return render(request, 'easy_booking/register.html', {'form': form})

# Landing

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('create_booking')  # If logged in, redirect to booking page
    return render(request, 'easy_booking/landing_page.html')  # Otherwise, show landing page