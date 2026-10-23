class DomainError(Exception):
    """Base de todos los errores de negocio esperados.
    Su mensaje es seguro de mostrar al usuario."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje


class RecursoNoEncontrado(DomainError):
    """El registro pedido no existe o no pertenece a la barbería."""


class ReglaDeNegocioError(DomainError):
    """Se intentó algo que las reglas del negocio no permiten."""