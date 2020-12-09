from rest_framework import viewsets
from rest_framework import filters
from .models import Address
from .serializers import AddressSerializer
from .permission import IsReadOnly
from rest_framework.permissions import IsAdminUser


class AddressViewSet(viewsets.ModelViewSet):
    """
    Address view.
    """
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    permission_classes = (IsReadOnly|IsAdminUser, )

    search_fields = ['id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number']
    ordering_fields = search_fields

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

        