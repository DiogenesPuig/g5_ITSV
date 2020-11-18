from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import Hotel

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Proyecto/home.html'


def hotel(request):
    hotel= Hotel.objects.get(id=1)
    return render(request, 'Proyecto/home.html',{'name': request.user, 'hotel': hotel.nombre,'estrellas':hotel.estrellas,'direccion':hotel.direccion})