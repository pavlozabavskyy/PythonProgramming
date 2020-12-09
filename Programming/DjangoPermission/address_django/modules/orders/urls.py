from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet

router = DefaultRouter()
router.register(r'orders', OrdersViewSet, basename='user')

urlpatterns = router.urls
