from django.urls import include, path

from users.api.router import router

app_name = "users"

urlpatterns = [
    path("", include(router.urls)),
]
