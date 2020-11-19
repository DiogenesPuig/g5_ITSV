from django.urls import path,include
from Proyecto.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
