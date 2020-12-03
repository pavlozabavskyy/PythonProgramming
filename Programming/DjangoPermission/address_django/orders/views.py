from rest_framework import viewsets
from rest_framework import filters
from .models import Orders
from .serializers import OrdersSerializer
from rest_framework.permissions import IsAuthenticated


class OrdersViewSet(viewsets.ModelViewSet):
    """
    Orders view with search, ordering. Permission - authenticated user.
    """
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)

    search_fields = ['amount', 'date', 'item']
    ordering_fields = search_fields

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    