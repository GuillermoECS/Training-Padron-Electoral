from django.db import models

# Create your models here.

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from location_field.models.plain import PlainLocationField
# Import for the validators
from .validators import validate_email
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator

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


class Provincia(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=1, primary_key=True)
    nombre = models.TextField(
        _('Provincia'), max_length=30)

class Canton(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=1, primary_key=True)
    nombre = models.TextField(
        _('Canton'), max_length=30)

class Distrito(models.Model):
    codigo = models.SmallIntegerField(default=0, max_length=1, primary_key=True)
    nombre = models.TextField(
        _('Distrito'), max_length=30)

class Codigo_electoral(models.Model):
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