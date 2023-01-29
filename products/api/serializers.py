from rest_framework.serializers import ModelSerializer

from products.models import Product
from categories.api.serializers import CategorySerializer


class ProductSerializer(ModelSerializer):
    category_data = CategorySerializer(source="category", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "image",
            "price",
            "category",
            "category_data",
            "active",
        ]
