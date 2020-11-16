from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Address
from .serializers import AddressSerializer

class AddressView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response({"addresses": serializer.data})

    def post(self, requst):
        address = requst.data.get('address')

        serializer = AddressSerializer(data=address)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"success": "Address '{}' created successfully".format(address_saved.address_line)})