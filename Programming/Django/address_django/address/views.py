from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    search_fields = ['id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number']
    ordering_fields = search_fields

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
