from django.urls import path
from .views import AddressView

app_name = "addresses"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('addresses/', AddressView.as_view()),
    path('addresses/<int:pk>', AddressView.as_view())
]