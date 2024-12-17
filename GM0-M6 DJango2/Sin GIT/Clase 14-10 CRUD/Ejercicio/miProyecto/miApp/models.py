from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return self.titulo


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    sitio_web = models.CharField(max_length=250)
    telefono = models.IntegerField()

    def __str__(self):
        return self.user.get_username()
