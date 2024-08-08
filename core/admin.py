from django.contrib import admin
from .models import CustomUser, Parcel, TravelDetails, Review

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Parcel)
admin.site.register(TravelDetails)
admin.site.register(Review)
