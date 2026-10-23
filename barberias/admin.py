from django.contrib import admin

from planes.models import Funcionalidad, Plan


@admin.register(Funcionalidad)
class FuncionalidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ("nombre", "codigo")


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "precio_mensual", "max_barberos", "es_publico", "orden")
    list_editable = ("precio_mensual", "es_publico", "orden")
    filter_horizontal = ("funcionalidades",)