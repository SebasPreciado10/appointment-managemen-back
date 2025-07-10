from core.models.status import Status
from core.exceptions.status_exceptions import StatusAlreadyExists, StatusNotFound

def create_status(validated_data):
    name = validated_data.get("name")
    if Status.objects.filter(name__iexact=name).exists():
        raise StatusAlreadyExists()
    return Status.objects.create(**validated_data)

def list_statuses():
    return Status.objects.all()

def update_status(validated_data):
    try:
        status_obj = Status.objects.get(id=validated_data["id"])
    except Status.DoesNotExist:
        raise StatusNotFound()
    status_obj.name = validated_data["name"]
    status_obj.save()
    return status_obj

def delete_status(status_id):
    try:
        status_obj = Status.objects.get(id=status_id)
    except Status.DoesNotExist:
        raise StatusNotFound()
    status_obj.delete()
    return status_obj