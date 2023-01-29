from rest_framework.routers import DefaultRouter

from payments.api.viewsets import PaymentViewSet

router = DefaultRouter()

router.register(r"payments", PaymentViewSet, basename="payments")