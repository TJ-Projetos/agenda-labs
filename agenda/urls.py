from django.contrib import admin
from django.urls import path
from .views import *
from .entidades.agenda import Agenda
urlpatterns = [
    path('agenda/manha',agenda1,name="agenda1"),
    path('pagina_cadastro',mostrar_form,name="mostrar_form"),
    path('login',login,name="login"),
    #path('criar_horarios',criarHorarios,name="criarHorarios"), #cadastrar todos os horarios
]
