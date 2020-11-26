from django.urls import path,include

from Proyecto.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView, name='login'),
    path('register', RegisterView,name='register'),
    path('logout',LogoutUser,name="logout"),
    path('hoteles/<str:Hotel>/',HotelesView,name="hoteles"),
    path('habitacion/<str:Habitacion>/',HabitacionView,name='habitaciones'),
    path('reservar/<str:Habitacion>/',hacerReserva,name='reservar')

]
