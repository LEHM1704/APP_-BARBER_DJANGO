from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    fecha_eliminado = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        
    def sof_delete(self):
        self.eliminado = True
        self.fecha_eliminado = timezone.now()
        self.save(update_fields=["eliminado", "fecha_eliminacion", "actualizado_en"])
        
        