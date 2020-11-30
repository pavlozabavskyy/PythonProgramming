from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Address
        fields = '__all__' 

