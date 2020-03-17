from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.shortcuts import render, redirect
from .forms import *
from .entidades.agenda import *
from .services import agenda_services
# Create your views here.

@login_required
def agendar(request):
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
				return redirect('mostrar_agenda')
			else:
				#return redirect('agendar')
				return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario,'mensagens':mensagens})
		else:
			return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario,'mensagens':mensagens})

	formulario = FormAgenda()
	return render(request, 'agenda/pagina_cadastro.html',{"formulario":formulario,'mensagens':mensagens})


@login_required
def mostrar_agenda(request):
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

def cadastar_usuario(request):
	sucesso=""
	mensagem=""
	form_usuario=UserCreationForm()
	if request.method == "POST":
		form_usuario = UserCreationForm(request.POST)
		if form_usuario.is_valid():
			usuario=form_usuario.save()
			usuario.is_active=False
			usuario.save()
			sucesso="ok"
		else:
			 mensagem=form_usuario.errors
	return render(request,'usuario/usr.html',{"usuario":form_usuario,"mensagem":mensagem,"sucesso":sucesso})


def logar(request):
	mensagem=""
	erro_login=""
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		usuario = authenticate(request, username=username,password=password)
		if usuario is not None:
			login(request,usuario)
			return redirect('mostrar_agenda')
		else:
			
			messages.error(request,"Usuario ou senha incoretos")
			return redirect('logar')	
	else:
		
		form_login = AuthenticationForm()
	return render(request,'usuario/login.html',{"usuario":form_login,"mensagem":mensagem,"erro":erro_login})

def deslogar(request):
	logout(request)
	return redirect('logar')