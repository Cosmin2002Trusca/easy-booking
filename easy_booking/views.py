from django.shortcuts import render
from django.views import generic
from .models import Table, Booking
# Create your views here.

class ReservationForm(generic.FormView):
    model = Booking