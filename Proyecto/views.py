from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import Hotel

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Proyecto/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        hotel= Hotel.objects.get(id=1)
        context["hotel"] = hotel
        return self.render_to_response(context)



def hotel(request):
    hotel= Hotel.objects.get(id=1)
    print("pase" + hotel)
    return render(request, 'Proyecto/home.html',{'name': request.user, 'hotel': "sheraton",'estrellas':hotel.estrellas,'direccion':hotel.direccion})
