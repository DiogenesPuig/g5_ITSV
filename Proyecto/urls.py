from django.urls import path,include

from Proyecto.views import *


urlpatterns = [
    path('',Pruebas,name="home"),
    path('hoteles/<str:Hotel>/',HotelesView2,name="hoteles"),
    path('login', LoginView, name='login'),
    path('register', RegisterView,name='register'),
    path('logout',LogoutUser,name="logout"),
    path('habitacion/<str:Habitacion>/',HabitacionView,name='habitaciones'),
    path('reservar/<str:Habitacion>/',hacerReserva,name='reservar'),
    path('deshacerReserva',deshacerReserva,name="deshacer_reserva"),
    path('elimnarrRserva/<str:Habitacion>',eliminarReserva,name='eliminar_reserva'),
]
