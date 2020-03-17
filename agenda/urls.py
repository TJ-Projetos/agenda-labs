from django.contrib import admin
from django.urls import path
from .views import *
from .entidades.agenda import Agenda
urlpatterns = [
    path('agenda/',mostrar_agenda,name="mostrar_agenda"),
    path('agendamento/',agendar,name="agendar"),
    path('cadastro/',cadastar_usuario,name="cadastar_usuario"),
    path('logar/',logar,name="logar"),
    path('logout/', deslogar, name="deslogar"),
    #path('criar_horarios',criarHorarios,name="criarHorarios"), #cadastrar todos os horarios
]
