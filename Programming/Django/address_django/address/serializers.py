from rest_framework import serializers

from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__' #('id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number')

