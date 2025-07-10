from rest_framework import serializers
from core.models.product_subline import ProductSubline

class ProductSublineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubline
        fields = ["name"]

class ProductSublineUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubline
        fields = ["id", "name"]

class ProductSublineResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubline
        fields = ["id", "name"]
