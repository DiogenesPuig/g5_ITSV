from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from Proyecto.models import *
import json

from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import path, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import CreateUserForm, UserForm, AlgoForm
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
        hotel = Hotel.objects.all()
        paginator = Paginator(hotelese, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        """jso = []
        hoteles = ""
        for hs in h:
            jso += {hs}
        cadena = json.dumps(jso)
        print(cadena)"""
        search_post = request.GET.get('search')
        str(search_post)
        if search_post:
            hotel = Hotel.objects.filter(Q(nombre__icontains=search_post))
        else:
            pass

        context['hoteles'] = page_obj

        query = request.GET.get('27')
        results = Habitacion.objects.filter(Q(num_habitacion=query))
        context['results'] = results
        context['hotel'] = hotel
        return self.render_to_response(context)


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
            p = Cliente(
                nombre=form.cleaned_data.get('first_name'),
                apellido=form.cleaned_data.get('last_name'),
                mail=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('username')
            )
            p.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'Proyecto/register.html', context)


def LogoutUser(request):
    logout(request)
    messages.success(request, "Has salido de tu sesion, gracias por elegirnos")
    return redirect('home')


def HotelesView(request, Hotel):
    from .models import Hotel as hotel
    hoteles = hotel.objects.get(pk=Hotel)  # Aca deberiamos llamar a las habitaciones del hotel que queremos
    order_by = request.GET.get('order_by')
    habitaciones = Habitacion.objects.all().order_by(order_by)
    h = hoteles.habitaciones
    paginator = Paginator(habitaciones, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    habs = Habitacion.objects.all()
    search_post = request.GET.get('search')
    str(search_post)
    if search_post:
        habs = Habitacion.objects.filter(Q(num_habitacion__icontains=search_post))
        str(habs)
    else:
        context = {
            'hoteles': hoteles,
            'habitaciones': page_obj,
            'h': h,
            'habs': habs,
        }
    ordering = ['-cant_dormitorios']    
    return render(request, 'Proyecto/hoteles.html', context, ordering)


def HabitacionView(request, Habitacion):
    from .models import Habitacion as habitacion
    habitaciones = habitacion.objects.get(pk=Habitacion)
    hotel = Hotel.objects.all()
    search_post = request.GET.get('search')
    str(search_post)
    if search_post:
        hotel = Hotel.objects.filter(Q(nombre__icontains=search_post))
    else:
        pass

    context = {
        'habitacion': habitaciones,
        'hotel': hotel,
    }
    return render(request, 'Proyecto/nos/habitaciones.html', context)


def hacerReserva(request, Habitacion):
    from .models import Habitacion as habitacion
    habi = habitacion.objects.get(pk=Habitacion)
    if request.user.is_authenticated:
        #Habitacion.estado = "Ocupado"
        #Habitacion.save()
        cliente = Cliente.objects.get(username=request.user.username)
        cliente.reservas.add(habi)
        cliente.save()
        cam = habitacion.objects.get(id=Habitacion)
        cam.estado = "Ocupado"
        cam.save()
        messages.success(request, "Tu reserva fue sido realizada con exito")
        return redirect('home')
    else:
        messages.error(request,"Tienes que estar logeado para hacer una reserva")
        return redirect('login')

    return redirect('home')
