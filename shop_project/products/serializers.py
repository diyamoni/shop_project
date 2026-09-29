from rest_framework import serializers
from.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']
        read_only_fields = ['id']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("The name is not empty.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price must be greater than 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("The stock is a valid number and cannot be negative.")
        return value