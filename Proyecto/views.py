from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import *
import json

from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator


from .forms import CreateUserForm, UserForm
from .models import *
from .models import Hotel
from django.views.generic import TemplateView
from django.db.models import Q

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Proyecto/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Creando publicaciones
        hotelese = Hotel.objects.all()
        paginator = Paginator(hotelese, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        """jso = []
        hoteles = ""
        for hs in h:
            jso += {hs}
        cadena = json.dumps(jso)
        print(cadena)"""
        context['hoteles'] = page_obj
        query = request.GET.get('27')
        results = Habitacion.objects.filter(Q(num_habitacion=query) | Q(estado=query)) 
        context['results'] = results
        return self.render_to_response(context)

    
    
    
    
    
    
    
    
   # def your_view(request):
    #This could be your actual view or a new one '''
    # Your code
    #    if request.method == 'GET': # If the form is submitted

     #       search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for

    # Your code
    

"""
def hotel(request):
    hotel = Hotel.objects.get(id=1)
    return render(request, 'Proyecto/home.html',
                  {'name': request.user, 'hotel': hotel.nombre, 'estrellas': hotel.estrellas,
                   'direccion': hotel.direccion})
"""


def LoginView(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password is incorrect ")
            return render(request, 'Proyecto/login.html', context)

    return render(request, 'Proyecto/login.html', context)



def RegisterView(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'Proyecto/register.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('login')

def HotelesView(request,Hotel):
    from .models import Hotel as hotel 
    hoteles = hotel.objects.get(pk=Hotel) #Aca deberiamos llamar a las habitaciones del hotel que queremos
    habitaciones = Habitacion.objects.all()
    h = hoteles.habitaciones
    paginator = Paginator(habitaciones, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context= {
        'hoteles':hoteles,
        'habitaciones':page_obj,
        'h': h,
    }
    return render(request,'Proyecto/hoteles.html',context)

def HabitacionView(request,Habitacion):
    from .models import  Habitacion as habitacion
    habitaciones = habitacion.objects.get(pk=Habitacion)
    hotel = Hotel.objects.all()
    search_post = request.GET.get('search')
    str(search_post)
    
   


    if search_post:
        
        hotel = Hotel.objects.filter(Q(nombre__icontains=search_post))

    else:

        print("hola")



    context= {
        'habitacion':habitaciones,
        'hotel': hotel,
    }

    
    return render(request,'Proyecto/ignore/habitaciones.html',context,)
