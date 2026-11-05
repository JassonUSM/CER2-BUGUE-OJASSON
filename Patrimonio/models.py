from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anioConstruccion = models.IntegerField()
    imagen = models.URLField(max_length=200, null=True)

    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


