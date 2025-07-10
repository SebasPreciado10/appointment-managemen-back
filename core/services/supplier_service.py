from core.models.supplier import Supplier
from core.exceptions.supplier_exceptions import SupplierAlreadyExists, SupplierNotFound

def create_supplier(validated_data):
    name = validated_data.get("name")
    if Supplier.objects.filter(name__iexact=name).exists():
        raise SupplierAlreadyExists("Proveedor ya existe.")
    return Supplier.objects.create(**validated_data)

def list_suppliers():
    return Supplier.objects.all()

def update_supplier(validated_data):
    try:
        supplier = Supplier.objects.get(id=validated_data["id"])
    except Supplier.DoesNotExist:
        raise SupplierNotFound("Proveedor no encontrado.")
    supplier.name = validated_data["name"]
    supplier.save()
    return supplier

def delete_supplier(supplier_id):
    try:
        supplier = Supplier.objects.get(id=supplier_id)
    except Supplier.DoesNotExist:
        raise SupplierNotFound("Proveedor no encontrado.")
    supplier.delete()
    return supplier
