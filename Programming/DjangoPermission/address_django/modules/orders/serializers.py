from rest_framework import serializers
from .models import Orders
from modules.address.models import Address


class OrdersSerializer(serializers.ModelSerializer):
    """
    Order serialiser.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Orders
        fields = ('user', 'item', 'amount', 'date')
    
    def create(self, validated_data):
        """ Address amount vs order amount. Update address. """
        address = validated_data['item']
        if address.amount == 0:
            raise serializers.ValidationError("No items left in stock")
        elif validated_data['amount'] > address.amount:
            raise serializers.ValidationError("Available quantity: {}".format(address.ammount))
           #validated_data['amount'] = address.amount

        # update item
        address.amount -= validated_data['amount']
        address.save()
        
        return Orders.objects.create(**validated_data)
    