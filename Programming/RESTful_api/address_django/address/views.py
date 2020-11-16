from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Address
from .serializers import AddressSerializer


"""class AddressView(viewsets.ViewSet):
    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def sort_by(self, request, attr=None):
        queryset = Address.objects.all().order_by('address_line')
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(user)
        return Response(serializer.data)
"""


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all().order_by('address_line')