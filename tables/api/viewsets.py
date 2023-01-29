from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from tables.api.serializers import TableSerializer
from tables.models import Table


class TableViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Table.objects.all().order_by("number")
    serializer_class = TableSerializer
