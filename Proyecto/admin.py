from django.contrib import admin
from Proyecto.models import *



class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','mail', 'telefono', 'codigo')

    
    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido', 'codigo')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
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
    list_display = ('precio_noche', 'num_habitacion', 'cant_dormitorios', 'cant_banios', 'estado', 'tipo_habitacion', 'img_habitacion')

'''
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_habitacion',)
'''

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estrellas', 'direccion')

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Hotel, HotelAdmin)
