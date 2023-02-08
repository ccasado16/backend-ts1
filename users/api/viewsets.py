from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # request.data._mutable = True
        request.data["password"] = make_password(request.data["password"])
        # request.data._mutable = True

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # request.data._mutable = True

        password = request.data["password"]

        if password:
            request.data["password"] = make_password(password)
        else:
            request.data["password"] = request.user.password

        # request.data._mutable = False

        return super().update(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
