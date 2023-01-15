from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    def __str__(self):
            return f"Nombre: {self.nombre} - Apellido {self.camada} - Email {self.camada} - Profesion {self.camada} "

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
