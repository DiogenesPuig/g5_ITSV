from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return ": " + str(self.calle) + " " + str(self.altura)        

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, default = None, blank = True, null = True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Cliente(Persona):
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return ": " + str(self.nombre)     

class Administrador(Persona):
    codigo = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'


class Estado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status=[
    ('Disponible','D'),
    ('Ocupado','O'),
    ]
    estado = models.CharField(max_length = 50,choices = status, default='Disponible')

    def __str__(self):
        return ": " + str(self.estado)    

class TipoHabitacion(models.Model):
    tipoHabitacion = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Tipo de Habitacion'
        verbose_name_plural = 'Tipos de Habitaciones'

    def __str__(self):
        return ": " + str(self.tipoHabitacion)     

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
    
    def __str__(self):
        return ": " + str(self.numHabitacion)        

class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    habitaciones = models.ForeignKey(Habitacion, on_delete=models.CASCADE, default = None, blank = True, null = True)
    direccion =  models.ForeignKey(Direccion, on_delete=models.CASCADE, default = None, blank = True, null = True)     

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

# Create your models here.
