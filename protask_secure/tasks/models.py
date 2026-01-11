from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('C', 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    prioridad = models.IntegerField(default=1)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
