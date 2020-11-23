from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Address
from .serializers import AddressSerializer
from .permision import IsOwnerOrReadOnly

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    permission_classes = (IsOwnerOrReadOnly, )

    search_fields = ['id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number']
    ordering_fields = search_fields

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
