from django.db import models

class Recompensa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_necesarios = models.IntegerField()

    def __str__(self):
        return self.nombre