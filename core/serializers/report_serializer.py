
# core/serializers/report_serializer.py
from rest_framework import serializers
from core.models.report import Report

class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['product_subline']
        

class ReportResponseSerializer(serializers.ModelSerializer):
    product_subline_name = serializers.CharField(source='product_subline.name', read_only=True)
    average_delivery_time_decimal = serializers.SerializerMethodField()
    average_delivery_time_readable = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            "id",
            "generated_at",
            "average_delivery_time_decimal",
            "average_delivery_time_readable",
            "product_subline_name"
        ]

    def get_average_delivery_time_decimal(self, obj):
        return round(obj.average_delivery_time / 60, 2)

    def get_average_delivery_time_readable(self, obj):
        total_minutes = int(obj.average_delivery_time)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours}h {minutes}m"