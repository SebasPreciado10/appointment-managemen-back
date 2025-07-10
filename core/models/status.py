from django.db import models
from core.utils.uuid import generate_uuid

class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.name