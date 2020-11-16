from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet

#app_name = "addresses"
# app_name will help us do a reverse look-up latter.

"""urlpatterns = [
    path('addresses/', AddressView.as_view({'get': 'list'})),
    path('addresses/sort_by/<str:attr>', AddressView.as_view({'get': 'sort_by'})),
    path('addresses/<int:pk>', AddressView.as_view({'get': 'retrieve'})),
]"""

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='user')

urlpatterns = router.urls