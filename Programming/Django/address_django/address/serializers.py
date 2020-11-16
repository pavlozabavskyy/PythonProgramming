from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number')

