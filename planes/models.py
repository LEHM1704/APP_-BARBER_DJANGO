from django.db import models

from core.models import BaseModel


class Funcionalidad(BaseModel):
    codigo = models.SlugField(unique=True)  # lo usa el código: "inventario", "crm"
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "funcionalidad"
        verbose_name_plural = "funcionalidades"

    def __str__(self):
        return self.nombre


class Plan(BaseModel):
    codigo = models.SlugField(unique=True)
    nombre = models.CharField(max_length=60)
    precio_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    max_barberos = models.PositiveIntegerField(
        null=True, blank=True, help_text="Vacío = ilimitado"
    )
    funcionalidades = models.ManyToManyField(
        Funcionalidad, blank=True, related_name="planes"
    )
    es_publico = models.BooleanField(default=True)
    orden = models.PositiveSmallIntegerField(default=0)

    class Meta:

        ordering = ["orden"]

    def __str__(self):
        return self.nombre