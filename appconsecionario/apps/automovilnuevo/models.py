from django.db import models
from django.db import clientes

# Create your models here.
class automovilnuevo(models.model):

matricula = models.VarcharFile(max_length=45)
modelo = models.CharFile(max_length=50)
marca = models.CharFile(max_length=45)
color = models.CharFile(max_length=50)
num_vehiculo = models.IntFile()
clientes = models.ForeignKey(clientes, verbose_name="cliente", null=True, blank=True, on_delete=CASCADE)
def __str__(self):
        texto = "{0},{1},{2},{3},{4}"
        return texto.format(self.automovilnuevo, self.matricula, self.modelo, self.marca, self.color, self.num_vehiculo)

        
def __str__(self):
        texto = "{0}"
        return texto.format(self.automovilnuevo)