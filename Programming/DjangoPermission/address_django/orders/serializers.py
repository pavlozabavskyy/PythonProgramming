from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Orders
        fields = '__all__'  