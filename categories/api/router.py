from rest_framework.routers import DefaultRouter

from categories.api.viewsets import CategoryViewSet

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="categories")
