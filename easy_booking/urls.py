from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationForm.as_view(), name ="home"),
]