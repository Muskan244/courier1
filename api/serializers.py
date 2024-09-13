from rest_framework import serializers
from core.models import Parcel, PNR

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('sender', 'traveling_user', 'description', 'weight', 'destination', 'deadline')

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('sender', 'traveling_user', 'description', 'weight', 'destination', 'deadline')

class PNRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNR
        fields = ["pnr_number", "is_valid"]

    def validate_pnr_number(self, value):
        if not value.startswith('1'):
            raise serializers.ValidationError("PNR must start with '1'")
        elif len(value) != 10:
            raise serializers.ValidationError("PNR must have 10 letters")
        return value