from django.db import models
from .product_subline import ProductSubline
from core.utils.uuid import generate_uuid

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    generated_at = models.DateTimeField(auto_now_add=True)
    average_delivery_time = models.FloatField()
    product_subline = models.ForeignKey(ProductSubline, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'report'


    def __str__(self):
        return f"Reporte - {self.product_subline.name} - {self.average_delivery_time:.2f} hrs"
