from rest_framework import serializers
from circon.warehouse.products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('products', 'category')
