from django.contrib import admin
from Proyecto.models import *



class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','mail', 'telefono', 'codigo')

    
    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido', 'codigo','reservas')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
        })
    )

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','mail', 'telefono', 'codigo')

    
    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido', 'codigo',)
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
        })
    )


class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('precio_noche', 'num_habitacion', 'cant_dormitorios', 'cant_banios', 'estado', 'tipo_habitacion', 'img_habitacion','descripcion')

'''
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipo_habitacion',)
'''

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estrellas', 'direccion', 'img_hotel',)

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Hotel, HotelAdmin)
