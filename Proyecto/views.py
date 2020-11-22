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
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Proyecto/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Creando publicaciones
        hoteles = Hotel.objects.all()
        paginator = Paginator(hoteles, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        """jso = []
        hoteles = ""
        for hs in h:
            jso += {hs}
        cadena = json.dumps(jso)
        print(cadena)"""
        context['hotel'] = page_obj
        return self.render_to_response(context)

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

def HotelesView(request):
    hoteles = Hotel.objects.all()
    habitaciones = Habitacion.objects.all()

    context= {
        'hoteles':hoteles,
        'habitaciones':habitaciones
    }
    return render(request,'Proyecto/hoteles.html',context)
