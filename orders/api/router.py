from rest_framework.routers import DefaultRouter

from orders.api.viewsets import OrderViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")
