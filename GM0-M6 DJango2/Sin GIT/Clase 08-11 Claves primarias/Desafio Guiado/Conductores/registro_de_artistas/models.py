from django.db import models


class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    fecha_creacion = models.DateField(null=False)
    artistas = models.ManyToManyField(
        "Artista", through="ArtistaGrupo", related_name="grupos"
    )

    def __str__(self):
        return self.nombre


class ArtistaGrupo(models.Model):
    artista_id = models.ForeignKey(Artista, on_delete=models.DO_NOTHING)
    grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField(auto_now_add=True)
    agregado_por = models.DateField()


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    grupo_id = models.ForeignKey(
        Grupo, null=False, blank=False, related_name="albumes", on_delete=models.CASCADE
    )
