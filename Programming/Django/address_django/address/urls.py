from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AddressViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='user')

urlpatterns = router.urls