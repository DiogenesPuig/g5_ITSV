from django.contrib import admin
from Proyecto.models import *





class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','mail', 'telefono', 'codigo')

    
    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido', 'codigo')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail', 'direccion')
        })
    )

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','mail', 'telefono', 'codigo')

    
    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido', 'codigo')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
        })
    )
    
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'estado')    

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('precioNoche', 'numHabitacion', 'cantDormitorios', 'cantBanios', 'estado', 'tipohabitacion', 'img_habitacion')

class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipoHabitacion',)


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Direccion,)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
