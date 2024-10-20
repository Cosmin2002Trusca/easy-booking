from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_easy_booking(request):
    return HttpResponse("Hello, world!")