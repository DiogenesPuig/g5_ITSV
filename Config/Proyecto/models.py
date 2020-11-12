from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Cliente(Persona):
    codigo = models.CharField(max_length=20)

class Administrador(Persona):
    codigo = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

class Estado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status=[
    ('Disponible','D'),
    ('Ocupado','O'),
    ]
    estado = models.CharField(max_length = 50,choices = status, default='Disponible')

class TipoHabitacion(models.Model):
    tipoHabitacion = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Tipo de Habitacion'
        verbose_name_plural = 'Tipos de Habitaciones'

class Habitacion(models.Model):
    precioNoche = models.IntegerField()
    numHabitacion = models.IntegerField()
    cantDormitorios = models.IntegerField()
    cantBanios = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,default=None)
    tipohabitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE,default=None)
    img_habitacion = models.ImageField(max_length=100, upload_to='img_habitacion/', blank=True)
    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

# Create your models here.
