from core.models.product_subline import ProductSubline
from core.exceptions.product_subline_exceptions import (
    ProductSublineAlreadyExists,
    ProductSublineNotFound,
)

def create_product_subline(validated_data):
    name = validated_data.get("name")
    if ProductSubline.objects.filter(name__iexact=name).exists():
        raise ProductSublineAlreadyExists()
    return ProductSubline.objects.create(**validated_data)

def list_product_sublines():
    return ProductSubline.objects.all()

def update_product_subline(validated_data):
    subline_id = validated_data.get("id")
    try:
        subline = ProductSubline.objects.get(id=subline_id)
    except ProductSubline.DoesNotExist:
        raise ProductSublineNotFound()
    for attr, value in validated_data.items():
        setattr(subline, attr, value)
    subline.save()
    return subline

def delete_product_subline(subline_id):
    try:
        subline = ProductSubline.objects.get(id=subline_id)
    except ProductSubline.DoesNotExist:
        raise ProductSublineNotFound()
    subline.delete()
    return subline
