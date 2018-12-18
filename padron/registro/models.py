from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Persona(models.Model):
    cedula = models.TextField(
        _('Cedula'), max_length=9, primary_key=True)
    sexo =  models.TextField(
        _('Sexo'), max_length=9)
    codigo_electoral = models.SmallIntegerField(default=0, max_length=6)
    fecha_nacimiento = models.DateTimeField()
    junta = models.SmallIntegerField(default=0, max_length=5)
    nombre = models.TextField(
        _('Nombre'), max_length=30)
    apellido_1 = models.TextField(
        _('Apellido1'), max_length=26)
    apellido_2 = models.TextField(
        _('Apellido2'), max_length=26)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')

class Provincia(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=1, primary_key=True)
    nombre = models.TextField(
        _('Provincia'), max_length=10)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')

class Canton(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=2, primary_key=True)
    nombre = models.TextField(
        _('Canton'), max_length=20)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Canton')
        verbose_name_plural = _('Cantones')

class Distrito(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=3, primary_key=True)
    nombre = models.TextField(
        _('Distrito'), max_length=34)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Distrito')
        verbose_name_plural = _('Distritos')

class Codigo_Electoral(models.Model):
    provincia = models.OneToOneField(
        Provincia,
        on_delete=models.CASCADE,
    )
    canton = models.OneToOneField(
        Canton,
        on_delete=models.CASCADE,
    )
    distrito = models.OneToOneField(
        Distrito,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Codigo electoral')
        verbose_name_plural = _('Codigos electorales')

class RegistroProvincia(models.Model):
    provincia= models.OneToOneField(
        Provincia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Registro de provincia')
        verbose_name_plural = _('Registros de provincia')

class RegistroCanton(models.Model):
    canton = models.OneToOneField(
        Canton,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Registro de canton')
        verbose_name_plural = _('Registros de canton')


class RegistroDistrito(models.Model):
    distrito = models.OneToOneField(
        Distrito,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Registro de distrito')
        verbose_name_plural = _('Registros de distrito')

class RegistroCodigoElectoral(models.Model):
    codigo_electoral = models.OneToOneField(
        Codigo_Electoral,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Registro de codigo electoral')
        verbose_name_plural = _('Registros de codigos electorales')

class RegistroVencimiento(models.Model):
    vencimiento = models.DateField(default=0, primary_key=True)
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Vencimiento')
        verbose_name_plural = _('Vencimientos')

class RegistroSexo(models.Model):
    sexo = models.IntegerField(default=0, primary_key=True)
    cantidad = models.IntegerField(max_length=50)

    class Meta:
        ordering = ('pk',)
        verbose_name = _('Registro de sexo')
        verbose_name_plural = _('Registros de sexo')