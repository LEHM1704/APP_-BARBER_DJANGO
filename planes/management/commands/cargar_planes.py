from django.core.management.base import BaseCommand
from django.db import transaction

from planes.models import Funcionalidad, Plan

# Valores iniciales PROVISIONALES: se ajustan desde el panel de administración.
FUNCIONALIDADES = [
    {"codigo": "inventario", "nombre": "Inventario", "descripcion": "Control de productos y stock"},
    {"codigo": "crm", "nombre": "CRM de clientes", "descripcion": "Seguimiento y recuperación de clientes"},
]

PLANES = [
    {"codigo": "basico", "nombre": "Básico", "precio_mensual": 39,
     "max_barberos": 2, "orden": 1, "funcionalidades": []},
    {"codigo": "profesional", "nombre": "Profesional", "precio_mensual": 69,
     "max_barberos": 6, "orden": 2, "funcionalidades": ["inventario"]},
    {"codigo": "premium", "nombre": "Premium", "precio_mensual": 99,
     "max_barberos": None, "orden": 3, "funcionalidades": ["inventario", "crm"]},
]


class Command(BaseCommand):
    help = "Crea los planes y funcionalidades iniciales. Es seguro ejecutarlo varias veces."

    @transaction.atomic
    def handle(self, *args, **options):
        funcionalidades = {}
        for datos in FUNCIONALIDADES:
            obj, _ = Funcionalidad.objects.get_or_create(
                codigo=datos["codigo"],
                defaults={"nombre": datos["nombre"], "descripcion": datos["descripcion"]},
            )

            funcionalidades[obj.codigo] = obj

        for datos in PLANES:
            plan, creado = Plan.objects.get_or_create(
                codigo=datos["codigo"],
                defaults={
                    "nombre": datos["nombre"],
                    "precio_mensual": datos["precio_mensual"],
                    "max_barberos": datos["max_barberos"],
                    "orden": datos["orden"],
                },
            )
            if creado:
                plan.funcionalidades.set(
                    [funcionalidades[c] for c in datos["funcionalidades"]]
                )
                self.stdout.write(self.style.SUCCESS(f"Plan creado: {plan.nombre}"))
            else:
                self.stdout.write(f"Plan ya existía, sin cambios: {plan.nombre}")