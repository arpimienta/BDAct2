from django.db import models
from apps.automovilnuevo import automovilnuevo
from apps.automovilviejos import automovilviejos 
# Create your models here.

class controldereparacion(models.model):

f_reparacion= models.DateFile()
hora_reparacion = models.TimeFile()
mecanico = models.ForeignKey(clientes, verbose_name="mecanico", null=True, blank=True, on_delete=CASCADE)


def __str__(self):
        texto = "{0},{1}"
        return texto.format(self.controldereparacion, self.f_reparacion, self.hora_reparacion)

        
def __str__(self):
        texto = "{0}"
        return texto.format(self.controldereparacion)
