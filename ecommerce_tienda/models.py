from django.db import models

# Create your models here.

class Product(models.Model):
    Producto = models.CharField(max_length=200)
    Costo = models.IntegerField()
    Cantidad = models.PositiveIntegerField(default=1)
    Descripcion = models.TextField(blank=True,null=True)

