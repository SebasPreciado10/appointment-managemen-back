from rest_framework import serializers
from core.models.status import Status

class StatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["name"]


class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]


class StatusResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]