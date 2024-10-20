from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    """Represents a restaurant table."""
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Booking(models.Model):
    """Represents a customer reservation."""
    # Basic customer details
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15, blank=True, null=True)

    # Reservation details
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    # Optional special requests or comments
    special_request = models.TextField(blank=True, null=True)

    # Auto timestamp when the booking was made
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensures no double-booking for the same table at the same time
        unique_together = ('table', 'booking_date', 'booking_time')
        ordering = ['booking_date', 'booking_time']

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date} at {self.booking_time}"