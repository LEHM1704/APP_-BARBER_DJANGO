from django.contrib.auth.base_user import BaseUserManager


class UsuarioManager(BaseUserManager):
    """Crea usuarios que se identifican por correo en lugar de username."""

    def _crear(self, email, password, **campos):
        if not email:
            raise ValueError("El correo es obligatorio")
        email = self.normalize_email(email).lower()
        usuario = self.model(email=email, **campos)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **campos):
        campos.setdefault("is_staff", False)
        campos.setdefault("is_superuser", False)
        return self._crear(email, password, **campos)

    def create_superuser(self, email, password=None, **campos):
        campos.setdefault("is_staff", True)
        campos.setdefault("is_superuser", True)
        if not (campos["is_staff"] and campos["is_superuser"]):
            raise ValueError("Un superusuario debe tener is_staff e is_superuser en True")
        return self._crear(email, password, **campos)