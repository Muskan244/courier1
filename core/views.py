from django.shortcuts import render
from .models import Review, CustomUser, Parcel, TravelDetails
from django.utils import timezone

# Create your views here.
def home_page(request):
    parcels = Parcel.objects.all()
    travel_details = TravelDetails.objects.all()
    return render(request, 'core/home_page.html', {'parcels': parcels, 'travel_details': travel_details})

def index(request):
    return render(request, 'core/index.html', {})

def sign_in(request):
    return render(request, 'core/index.html', {})