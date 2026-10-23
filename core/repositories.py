from core.exceptions import RecursoNoEncontrado


class BaseRepository:
    """Acceso a datos de un modelo, siempre limitado a una barbería."""

    model = None  # cada repository hijo declara su modelo

    def __init__(self, barberia):
        self.barberia = barberia

    def _queryset(self):
        return self.model.objects.filter(barberia=self.barberia, eliminado=False)

    def listar(self):
        return self._queryset()

    def obtener(self, pk):
        try:
            return self._queryset().get(pk=pk)
        except self.model.DoesNotExist:
            raise RecursoNoEncontrado(f"{self.model._meta.verbose_name.capitalize()} no encontrado")

    def crear(self, **datos):
        return self.model.objects.create(barberia=self.barberia, **datos)

    def eliminar(self, instancia):
        instancia.soft_delete()