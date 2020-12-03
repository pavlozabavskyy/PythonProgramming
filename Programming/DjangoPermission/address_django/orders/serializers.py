from rest_framework import serializers
from .models import Orders
from address.models import Address


class OrdersSerializer(serializers.ModelSerializer):
    """
    Order serialiser.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Orders
        fields = ('user', 'item', 'amount', 'date')
    
    def create(self, validated_data):
        """ Check item amount and order amount. Update him. """
        address = validated_data['item']
        if validated_data['amount'] > address.amount:
           validated_data['amount'] = address.amount

        # update item
        address.amount -= validated_data['amount']
        address.save()
        
        return Orders.objects.create(**validated_data)
    