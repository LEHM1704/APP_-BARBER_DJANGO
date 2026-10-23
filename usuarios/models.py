from django.contrib.auth.models import AbstractUser
from django.db import models

from usuarios.managers import UsuarioManager


class Usuario(AbstractUser):
    username = None
    email = models.EmailField("correo", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = "usuario"

    def __str__(self):
        return self.email