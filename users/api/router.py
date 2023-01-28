from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api.viewsets import UserViewSet, UserView

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("auth/me/", UserView.as_view()),
]
