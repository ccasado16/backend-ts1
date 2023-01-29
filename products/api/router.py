from rest_framework.routers import DefaultRouter

from products.api.viewsets import ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
