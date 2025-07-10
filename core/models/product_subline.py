from django.db import models
from core.utils.uuid import generate_uuid

class ProductSubline(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'product_subline'

    def __str__(self):
        return self.name