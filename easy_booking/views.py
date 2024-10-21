from django.shortcuts import render
from django import forms
from django.views import generic
from .models import Booking, Table
# Create your views here.

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