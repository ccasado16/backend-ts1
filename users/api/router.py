from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api.viewsets import UserViewSet, UserView

from rest_framework_simplejwt.views import TokenObtainPairView # add for JWTAuthentication

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # add to path for the users jwt
    path("auth/me/", UserView.as_view()),
]
