from django.db import models
from django.contrib.auth.models import User
from .supplier import Supplier
from .product_subline import ProductSubline
from .status import Status
from core.utils.uuid import generate_uuid

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    scheduled_delivery = models.DateTimeField()
    actual_delivery = models.DateTimeField(null=True, blank=True)
    
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    product_subline = models.ForeignKey(ProductSubline, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    
    remarks = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'appointment'

    def __str__(self):
        return f"Cita - {self.supplier.name} - {self.scheduled_delivery.strftime('%Y-%m-%d')}"
