from rest_framework import serializers
from core.models.appointment import Appointment

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "scheduled_delivery",
            "actual_delivery",
            "supplier",
            "product_subline",
            "status",
            "remarks"
        ]

class AppointmentResponseSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)
    product_subline_name = serializers.CharField(source="product_subline.name", read_only=True)
    status_name = serializers.CharField(source="status.name", read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "scheduled_delivery",
            "actual_delivery",
            "remarks",
            "supplier_name",
            "product_subline_name",
            "status_name",
            "created_by_user",
            "created_at",
            "updated_at"
        ]

class AppointmentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "scheduled_delivery",
            "actual_delivery",
            "supplier",
            "product_subline",
            "status",
            "remarks"
        ]