from django.db import models

# Create your models here.

class mecanico(models.model):

DNI= models.IntFile()
nombre = models.CharFile(max_length=50)
apellido = models.CharFile(max_length=50)
f_contratacion = models.DateFile()
salario = models.IntFile()
automomilviejos=models ManyToManyField(automomilviejos, trough=mecanicoautomovilviejos)
automomilnuevo=models ManyToManyField(automomilnuevo, trough=mecanicoautomovilnuevo)

def __str__(self):
        texto = "{0},{1},{2},{3},{4}"
        return texto.format(self.mecanico, self.DNI, self.nombre, self.apellido, self.f_contratacion, self.salario)

        
def __str__(self):
        texto = "{0}"
        return texto.format(self.mecanico)



class mecanicoautomovilviejos(models.model):
        mecanico = models.ForeignKey(mecanico, verbose_name="mecanico", null=True, blank=True, on_delete=CASCADE)
        automomilviejos = models.ForeignKey(automomilviejos, verbose_name="automomilviejos", null=True, blank=True, on_delete=CASCADE)

class mecanicoautomovilnuevo(models.model):
        mecanico = models.ForeignKey(mecanico, verbose_name="mecanico", null=True, blank=True, on_delete=CASCADE)
        automomilnuevo = models.ForeignKey(automomilnuevo, verbose_name="automomilnuevo", null=True, blank=True, on_delete=CASCADE)
