from ..models import *

	
def salvar_agenda(agenda):
	agenda_bd=Agenda.objects.create(solicitante=agenda.solicitante,
		dias=agenda.dias,local_solicitado=agenda.local_solicitado,
		observacoes=agenda.observacoes)
	agenda_bd.save()
	for i in agenda.aulas:
		aula=Horarios.objects.get(id=i.id)
		agenda_bd.aulas.add(aula)


def salvar_dados():
	valores=["07:00 as 07:50","07:50 as 08:40","08:40 as 09:30","09:50 as 10:40","10:40 as 11:30",
	"11:30 as 12:20","13:20 as 14:10","14:10 as 15:00","15:00 as 15:50","16:10 as 17:00",
	"17:00 as 17:50","17:50 as 18:40","18:10 as 19:00","19:00 as 19:50","19:50 as 20:40",
	"20:50 as 21:40","21:40 as 22:30"]
	for valor in valores:
		Horarios.objects.create(intervalo=valor)
				
	dias=["Segunda-Feira", "Terça-Feira","Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
	for dia in dias:
		Dia.objects.create(dia_semana=dia)

	locais=["Laboratório de Informática", "Laboratório de Redes de Computadores", "Laboratório de Arquitetura de Computadores"]
	for local in locais:
		Local.objects.create(nome=local)



def retornar_horarios():
	horarios=Horarios.objects.all()
	return horarios

def retornar_agenda(lab="Laboratório de Informática"):
	""" Retorna agendamentos por local e 
	prepara a estrutura pra visualização"""
	local=Local.objects.get(nome=lab)

	agendas=Agenda.objects.filter(local_solicitado=local.id).all()
	horarios=Horarios.objects.all()
	dias=Dia.objects.all()
	estrutura={}
	for valor in horarios:
		estrutura[valor.intervalo]={}
	for valor in estrutura:
		for dia in dias:
			estrutura[valor][dia.id]="Livre"

	for agenda in agendas:
		# print(agenda.local_solicitado)
		for i in agenda.aulas.all():
			estrutura[i.intervalo][agenda.dias.id]=agenda.solicitante
	return estrutura


def verificar(agenda):
	lab=agenda.local_solicitado
	agenda_bd=retornar_agenda(lab)
	# print(lab)
	lista=[]

	for i in agenda.aulas:
		if agenda_bd[str(i)][agenda.dias.id] != "Livre":
			lista.append(i)
	return lista

def retornar_locais():
	locais=Local.objects.all()
	return locais

