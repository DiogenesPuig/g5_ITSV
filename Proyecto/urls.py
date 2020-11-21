from django.urls import path,include
from Proyecto.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView, name='login'),
    path('register', RegisterView,name='register'),
    path('logout',LogoutUser,name="logout")
]
