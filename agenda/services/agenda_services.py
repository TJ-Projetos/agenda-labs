from ..models import Agenda, Horario, Vagas

def gerar_intervalo(aulas,inicio,fim):
	lista=[]
	for i in aulas:
		# print(aulas[i][:5:])
		# print()
		if str(inicio) in aulas[i][:5:]:
			print("Aula inicia no "+str(i)+"° horario")
			lista.append(i)
			print(i)
		if str(fim) in aulas[i][9::]:
			print("Aula termina no "+str(i)+"° horario")
			lista.append(i)
	lista=list(range(lista[0],lista[1]+1))
	return lista




def salvar_agenda(agenda):
	Agenda.objects.create(professor=agenda.professor,
		disciplina=agenda.disciplina,laboratorio=agenda.laboratorio,
		soft_uso=agenda.soft_uso,horario=agenda.horario,turno=agenda.turno, dia_semana=agenda.dia_semana)


def salvar_horario(horario):
	hora=Horario.objects.create(fim_uso=horario.fim_uso,
		inicio_uso=horario.inicio_uso)
	return hora


def retornar_agenda(alternar=1):
	if (alternar == 1):
		valores_alter={
			"07:00 as 07:50":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"07:50 as 08:40":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"08:40 as 09:30":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"09:50 as 10:40":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"10:40 as 11:30":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"11:30 as 12:20":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"}
			}
		aulas={1:"07:00 as 07:50",2:"07:50 as 08:40",3:"08:40 as 09:30",4:"09:50 as 10:40",5:"10:40 as 11:30",6:"11:30 as 12:20"}
	elif (alternar==2):
		valores_alter={
			"13:20 as 14:10":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"14:10 as 15:00":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"15:00 as 15:50":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"16:10 as 17:00":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"17:00 as 17:50":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"17:50 as 18:40":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"}
			}
		aulas={1:"13:20 as 14:10",2:"14:10 as 15:00",3:"15:00 as 15:50",4:"16:10 as 17:00",5:"17:00 as 17:50",6:"17:50 as 18:40"}
	elif(alternar==3):
		valores_alter={
			"18:10 as 19:00":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"19:00 as 19:50":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"19:50 as 20:40":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"20:50 as 21:40":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			"21:40 as 22:30":{1:"Livre",2:"Livre",3:"Livre",4:"Livre",5:"Livre"},
			}
		aulas={1:"18:10 as 19:00",2:"19:00 as 19:50",3:"19:50 as 20:40",4:"20:50 as 21:40",5:"21:40 as 22:30"}
	
	agenda=Agenda.objects.filter(laboratorio="1")
	# horario=Horario.objects.all()
	valores=[]
	for i in agenda:
		dia=i.dia_semana
		inicio=i.horario.inicio_uso.strftime('%H:%M')
		fim=i.horario.fim_uso.strftime('%H:%M')
		lista=[]
		for aula in aulas:
			if str(inicio) in aulas[aula][:8:]:
				# print("Aula inicia no "+str(aula)+"° horario")
				lista.append(aula)
			if str(fim) in aulas[aula][9::]:
				# print("Aula termina no "+str(aula)+"° horario")
				lista.append(aula)
			
		if lista != []:
			lista=list(range(lista[0],lista[1]+1))
		
		for indice in lista:
			valores_alter[aulas[indice]][int(dia)]=i.professor
	return valores_alter


def retornar_agenda_tarde(novo_horario):
	m={1:"07:00 as 07:50",2:"07:50 as 08:40",3:"08:40 as 09:30",4:"09:50 as 10:40",5:"10:40 as 11:30",6:"11:30 as 12:20"}
	t={1:"13:20 as 14:10",2:"14:10 as 15:00",3:"15:00 as 15:50",4:"16:10 as 17:00",5:"17:00 as 17:50",6:"17:50 as 18:40"}
	n={1:"18:10 as 19:00",2:"19:00 as 19:50",3:"19:50 as 20:40",4:"20:50 as 21:40",5:"21:40 as 22:30"}
	turno = novo_horario.inicio_uso.strftime('%H:%M')
	if turno in m.values():
		aulas=m
	elif turno in t.values():
		aulas=t
	elif  turno in t.values():
		aulas=n
	horario_bd=Horario.objects.all()
	
	valores=[]
	ocupados=[]
	for i in horario_bd:
		ocupados.append(i.dia_semana)
	if novo_horario.dia_semana not in ocupados:
		print("dia Livre")
	else:
		for i in horario_bd:
			dia=i.dia_semana
			if dia != novo_horario.dia_semana:
				continue
			else:
				inicio=novo_horario.inicio_uso.strftime('%H:%M')
				fim=novo_horario.fim_uso.strftime('%H:%M')
				inicio_bd=i.inicio_uso.strftime('%H:%M')
				fim_bd=i.fim_uso.strftime('%H:%M')
				valores_novos=gerar_intervalo(aulas,inicio,fim)
				valores_bd=gerar_intervalo(aulas,inicio_bd,fim_bd)

def cadastro_vagas():
	m={1:"07:00 as 07:50",2:"07:50 as 08:40",3:"08:40 as 09:30",4:"09:50 as 10:40",5:"10:40 as 11:30",6:"11:30 as 12:20"}
	for i in m.values():
		Vagas.objects.create(laboratorio="Redes de Computadores",turno="Manhã",intervalo=i,status="1")
