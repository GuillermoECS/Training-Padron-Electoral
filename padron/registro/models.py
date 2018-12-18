from django.db import models

# Create your models here.
class RegistroProvincia(models.Model):
    provincia= models.OneToOneField(
        Provincia,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=1
    )
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad


class RegistroCanton(models.Model):
    canton = models.OneToOneField(
        Canton,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=2
    )
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad

class RegistroDistrito(models.Model):
    distrito = models.OneToOneField(
        Distrito,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=3
    )
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad

class RegistroCodigoElectoral(models.Model):
    codigo_electoral = models.OneToOneField(
        CodigoElectoral,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=6
    )
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad

class RegistroVencimiento(models.Model):
    vencimiento = models.DateField()
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad

class RegistroSexo(models.Model):
    sexo = models.IntegerField(max_length=1)
    cantidad = models.IntegerField(max_length=50)

    def __str__(self):
        return self.cantidad