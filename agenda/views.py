from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from .entidades.agenda import *
from .services import agenda_services
# Create your views here.


def mostrar_form(request):
	mensagens=""
	if request.method =="POST":
		formulario = FormAgenda(request.POST)
		if formulario.is_valid():
			solicitante = formulario.cleaned_data["solicitante"]
			local_solicitado = formulario.cleaned_data["local_solicitado"]
			dias = formulario.cleaned_data["dia_semana"]
			aulas = formulario.cleaned_data["aulas"]
			observacoes = formulario.cleaned_data["observacoes"]
			nova_agenda=Agenda(solicitante=solicitante,local_solicitado=local_solicitado,
				dias=dias,aulas=aulas,observacoes=observacoes)
			mensagens=agenda_services.verificar(nova_agenda)
			if(not mensagens):
				agenda_services.salvar_agenda(nova_agenda)
				return redirect('agenda1')
			else:
				return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario,'mensagens':mensagens})
			
	formulario = FormAgenda()
	return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario,'mensagens':mensagens})



def agenda1(request):
	# agenda_services.salvar_dados()
	horarios=agenda_services.retornar_horarios()
	estrutura=agenda_services.retornar_agenda()
	locais=agenda_services.retornar_locais()
	dias=["SEGUNDA-FEIRA", "TERÇA-FEIRA","QUARTA-FEIRA", "QUINTA-FEIRA", "SEXTA-FEIRA"]
	turno="MANHÃ"
	local_default="Laboratório de Informática"
	if request.method == "POST" or None:
		local=request.POST.get("escolha")
		local_default=local
		estrutura=agenda_services.retornar_agenda(local)
		return render(request,'agenda/agendalabs_tabela.html',{'estrutura':estrutura,'dias':dias,
	 'turno':turno,'locais':locais,'local_default':local_default})
	else:
		return render(request,'agenda/agendalabs_tabela.html',{'estrutura':estrutura,'dias':dias,
			'turno':turno,'locais':locais,'local_default':local_default})

def login(request):
	form_usuario=UserCreationForm()
	if request.method == "POST":
		form_usuario = UserCreationForm(request.POST)
		if form_usuario.is_valid():
			form_usuario.save()

	return render(request,'usuario/usr.html',{"usuario":form_usuario})
