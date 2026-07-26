from django.db import models


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Palabra(models.Model):
    palabra_espanol = models.CharField(max_length=100)
    traduccion = models.CharField(max_length=100)

    descripcion = models.TextField(blank=True, null=True)

    idioma = models.ForeignKey(
        Idioma,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    imagen = models.ImageField(
        upload_to="palabras/",
        blank=True,
        null=True
    )

    audio = models.FileField(
        upload_to="audios/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.palabra_espanol