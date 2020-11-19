from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import *
import json


# Create your views here.
class HomeView(TemplateView):
    template_name = 'Proyecto/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Creando publicaciones
        h = Hotel.objects.all().values_list()
        jso = []
        hoteles = ""
        for hs in h:
            jso += {hs}
        cadena = json.dumps(jso)
        print(cadena)
        context['hotel'] = cadena
        return self.render_to_response(context)


def hotel(request):
    hotel = Hotel.objects.get(id=1)
    return render(request, 'Proyecto/home.html',
                  {'name': request.user, 'hotel': hotel.nombre, 'estrellas': hotel.estrellas,
                   'direccion': hotel.direccion})
