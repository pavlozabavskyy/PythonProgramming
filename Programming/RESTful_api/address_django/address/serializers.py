from rest_framework import serializers

from .models import Address

class AddressSerializer(serializers.Serializer):
    address_line = serializers.CharField()
    postal_code = serializers.DecimalField(max_digits=5, decimal_places=0)
    country = serializers.CharField()
    city = serializers.CharField()
    fax_number = serializers.CharField()
    phone_number = serializers.CharField()

    def create(self, validated_data):
        return Address.object,create(**validated_data)
