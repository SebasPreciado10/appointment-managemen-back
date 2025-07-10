from rest_framework import serializers
from core.models.supplier import Supplier

class SupplierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name"]

class SupplierResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name"]

class SupplierUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Supplier
        fields = ["id", "name"]