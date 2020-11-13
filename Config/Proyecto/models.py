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

    def __str__(self):
        return " " + str(self.nombre)     

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
        return " " + str(self.estado)    

class Habitacion(models.Model):
    precio_noche = models.IntegerField()
    num_habitacion = models.IntegerField()
    cant_dormitorios = models.IntegerField()
    cant_banios = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,default=None)
    status=[
    ('Suite', 'S'),
    ('Matrimonial', 'M'),
    ('Individual', 'I'),
    ('Familiar', 'F'),
    ('Normal', 'N'),
    ('Presidencial', 'P'),
    ]
    tipo_habitacion = models.CharField(max_length = 50,choices = status, default='Normal')
    img_habitacion = models.ImageField(max_length=100, upload_to='img_habitacion/', blank=True)


    
    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
    
    def __str__(self):
        return " " + str(self.num_habitacion)        

class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    habitaciones = models.ManyToManyField(Habitacion, default = None, blank = True)
    direccion = models.CharField(max_length=50, default = None, blank = True)    

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        return " " + str(self.nombre)        

# Create your models here.
