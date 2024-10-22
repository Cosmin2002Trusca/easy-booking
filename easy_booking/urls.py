from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, create_booking

urlpatterns = [
    path('register/', register, name='register'),  # Registration view
    path('login/', LoginView.as_view(template_name='easy_booking/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout view
    path('booking/', create_booking, name='create_booking'), #Booking
]