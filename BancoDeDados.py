from random import randint
from collections import defaultdict
codTEACHE = 0
codTeam = 0
codQuestion = 0


BDteams = {}
BDquestoes = {}
BDteacher = {}

class Teacher(object):
	Siape = 0

	__slots__ = ['siape','_name', '_email', '_password', 'teamUSERS', 'exerciciosID']
	def __init__(self,Email, Password, Name):
		print(Teacher.Siape)
		self.siape = str(Teacher.Siape)
		Teacher.Siape = int(Teacher.Siape)+1
		self._name = Name
		self._email = str(Email)
		self._password = str(Password)
		self.teamUSERS = []
		self.exerciciosID = []

	#Cadastrar Time
	def registerTeam(self, nameTeam, C1, C2, C3, C4):

		lista = []
		for x in BDteams.values():
			lista.append(str(x._nameTeam))

		if(nameTeam in lista):
			return False

		obj = Team(nameTeam, C1, C2, C3, C4, self.siape)
		BDteams[obj._user] = obj

		print("Time cadastrado")
		return True

	def registerQuestion(self, name, entrada, saida, desc, time):

		obj = Exercises(name, entrada, saida, desc, time)
		BDquestoes[obj._idQuestion] = obj
		self.exerciciosID.append(obj._idQuestion)

		print("Time cadastrado")
		return True

	def exerCadastrados(self,):
		return len(self.exerciciosID)

	def teamCadastrados(self):
		return len(self.teamUSERS)

	



def registerTeacher(email, password, name ):
	lista = []
	for x in BDteacher.values():
		lista.append(str(x._email))

	if(email in lista):
		return False

	obj = Teacher(email, password, name)
	BDteacher[obj.siape] = obj
	print("Professor(a) {} cadastrado(a).".format(obj._name))
	return True

def login(user, password):

	if( user in BDteams.keys()):
		if( BDteams[user]._password == password):
			print("Login Team Efetuado.")
			return ["Login Team Efetuado.",user, 1]
		print("Senha do team incorretos.")
		return ["Senha do team incorretos.",user, -1]

	if( user in BDteacher.keys()):
		if( BDteacher[user]._password == password):
			print("Login Teacher Efetuado.")
			return ["Login Teacher Efetuado.", user, 2]
		print("Senha do teacher incorreta.")
		return ["Senha do teacher incorreta.", user, -2]

	print("Login inexistente.")
	return ["Login inexistente.", 0, 0]

def showTable(self):
	print("Teams:", BDteams)
	print("Teacher", BDteacher)
	print("Questões", BDquestoes)

class Team(object):
	ID_team = 201807848

	__slots__ = ['idProf', '_user','_password','_components', '_nameTeam', '_corretas', '_historySubmit']
	def __init__(self, nameTeam, C1, C2, C3, C4, siape):
		self.idProf = siape
		self._user = str(Team.ID_team)
		Team.ID_team = str(Team.ID_team+(randint(500,999)))
		self._password = str(randint(10000, 99999)+randint(10000, 99999))
		self._components = [C1, C2, C3, C4]		#Lista de Students
		self._nameTeam = nameTeam
		self._corretas = 0
		self._historySubmit = []

	def pontuação(self):
		r = "{}/{}".format(self._corretas, len(BDteacher[self.idProf].exerCadastrados))
		print("pontuação", r)
		return r



####################################################################

class Exercises(object):
	Id_Local = 1
	def __init__(self, name, entrada, saida, desc, time):
		self._idQuestion = Exercises.Id_Local
		Exercises.Id_Local = Exercises.Id_Local+1
		self._nameQuestion = name
		self._entrada = entrada
		self._saida = saida
		self._desc = desc
		self._time = time
	#Alterar time de um exercicio