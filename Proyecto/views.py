from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import *
import json
from django.shortcuts import render 
from json import dumps 
from django.template.defaulttags import register
from django.http import HttpResponse


@register.filter
def get_item(dictionary, key):
    return HttpResponse(dictionary.get(key))


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




class HomeView2(HomeView):
    template_name = 'Proyecto/Hilton.html'


    