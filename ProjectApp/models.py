from django.db import models

# Create your models here.

class archivos(models.Model):
    nombre = models.CharField(max_length=50)
    extencion = models.CharField(max_length=20,null=True,blank=True)
    fecha = models.DateTimeField(auto_now_add = True)
    tamaño = models.IntegerField(null=True,blank=True)
    usuario = models.CharField(max_length=50,null=True,blank=True)
    archivo = models.FileField(upload_to = 'archivos')

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return self.nombre
