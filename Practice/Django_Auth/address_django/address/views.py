from rest_framework import viewsets
from rest_framework import filters
from .models import Address
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated


class AddressViewSet(viewsets.ModelViewSet):
    """
    Address view.
    """
    serializer_class = AddressSerializer

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    search_fields = ['id', 'address_line', 'postal_code', 'country', 'city', 'fax_number', 'phone_number']
    ordering_fields = search_fields

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    