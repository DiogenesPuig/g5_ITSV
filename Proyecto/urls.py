from django.urls import path,include
from Proyecto.views import HomeView
from Proyecto.views import HomeView2

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('page2', HomeView2.as_view(), name='page2')
]
