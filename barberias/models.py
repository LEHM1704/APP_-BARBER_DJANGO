from django.conf import settings
from django.db import models
from django.db.models import Q

from core.models import BaseModel


class Barberia(BaseModel):
    class Estado(models.TextChoices):
        PRUEBA = "prueba", "En prueba"
        ACTIVA = "activa", "Activa"
        VENCIDA = "vencida", "Vencida"

    nombre = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    plan = models.ForeignKey(
        "planes.Plan", on_delete=models.PROTECT, related_name="barberias"
    )
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PRUEBA)
    vence_el = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "barbería"
        verbose_name_plural = "barberías"

    def __str__(self):
        return self.nombre

class Membresia(BaseModel):
    class Rol(models.TextChoices):
        DUENO = "dueno", "Dueño"
        BARBERO = "barbero", "Barbero"
        RECEPCION = "recepcion", "Recepción"


    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="membresias"
    )
    barberia = models.ForeignKey(Barberia, on_delete=models.PROTECT, related_name="membresias")
    rol = models.CharField(max_length=20, choices=Rol.choices)
    atiende_citas = models.BooleanField(default=False)

    class Meta:
        verbose_name = "membresía"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "barberia"],
                condition=Q(eliminado=False),
                name="membresia_unica_activa",
            )
        ]

    def __str__(self):
        return f"{self.usuario} - {self.barberia} ({self.rol})"