from django.db import models

# Create your models here.

class clientes(models.model):

DNI= models.IntFile()
nombre = models.CharFile(max_length=50)
apellido = models.CharFile(max_length=50)
direccion = models.VarcharFile(max_length=45)
telefono = models.IntFile()

def __str__(self):
        texto = "{0},{1},{2},{3},{4}"
        return texto.format(self.clientes, self.nombre, self.apellido, self.direccion, self.telefono)

        
def __str__(self):
        texto = "{0}"
        return texto.format(self.clientes)