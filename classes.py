from random import randint

BDteams = {}
BDstudents = {}
BDteacher = {}

class Login(object):
	def __init__(self):
		self._teams = {}		#{Email:Senha}
		self._students = {}		#{Email:Senha}
		self._teacher = {}		#{Email:Senha}

	def login(self):
		User = input("Digite your email ou UserTeam: ")
		password = input("Digite your senha: ")
		
		if( User in self._teams.keys()):
			if( self._teams[User] == password):
				print("Login Team Efetuado.")
				return [1, self._user]
			print("Senha do team incorretos.")
			return [-1, self._user]

		if( User in self._students.keys()):
			if( self._students[User] == password):
				print("Login Student Efetuado.")
				return [2, self._matricula]
			print("Senha do student incorretos.")
			return [-2, self._matricula]

		if( User in self._teacher.keys()):
			if( self._teacher[User] == password):
				print("Login Teacher Efetuado.")
				return [3, self._siape]
			print("Senha do teacher incorretos.")
			return [-3, self._siape]

		print("Login inexistente.")
		return [0, None]

	def show(self):
		print("Teams:", self._teams)
		print("Student",self._students)
		print("Teacher",self._teacher)

	def registerTeacher(self):

		Email = input("Digite seu email: ")
		Password = input("Digite sua senha: ")
		Name = input("Digite nome completo: ")
		obj = Teacher(Email, Password, Name)
		self._teacher[Email] = Password
		
		BDteacher[obj._siape] = obj
		print("Professor(a) {} cadastrado(a).".format(Name))
		return True

	def registerStudent(self):

		Email = input("Digite seu email: ")
		Password = input("Digite sua senha: ")
		Name = input("Digite nome completo: ")
		Phone = input("Digite numero de telefone: ")
		obj = Student(Email, Password, Name, Phone)
		self._students[Email] = Password

		BDstudents[obj._matricula] = obj
		print("Estudante(a) {} cadastrado(a).".format(Name))
		return True
		
class Team(object):
	ID_team = 201807848

	__slots__ = ['_Components', '_Name']
	def __init__(self, Components, Name):
		self._user = str(Team.ID_team)
		Team.ID_team = str(Team.ID_team+(randint(500,999)))
		self._password = str(randint(10000, 99999)+randint(10000, 99999))
		self._components = []		#Lista de Students
		self._nameTeam = Name
		self._score = 0
		self._historySubmit = []

	#Metodos Professor
	#Recuperar Senha
	#Adicionar Componente
	'''
	def appendTeam(self):
		print("ID\tNome\tTime")
		for x,y in BDstudents.items():
			if(y._matricula not in self._teams.keys()):
				print("{}\t{}\t{}".format(y._matricula, y._name, y._team))
			print("-\t-\t-")
		name = input("Insira o nome do team: ")
		Id = list(map(str,input("Digite Matricula dos alunos que deseja adicionar neste team: ")))	
		for x in Id:
			if(x in self._students and x not in self._teams.keys())
			self._components.append(x)
	'''
	#Remover Componente
	#Get Score
	#Get historySubmit
	
	#Metodos Aluno
	#Submeter Respostas
	#Visualizar Historico
	#Visualizar Score

class Student(object):
	Matricula = 0

	__slots__ = ['_Email', '_Password', '_Name', '_Phone']
	def __init__(self, Email, Password, Name, Phone):
		self._matricula = str(Student.Matricula)
		Student.Matricula = str(Student.Matricula+1)
		self._email = str(Email)
		self._password = str(Password)
		self._name = Name
		self._phone = Phone
		self._subjects = []
		self._team = None		#Nome do Time

	def showStudent(self):
		print("Matricula\tNome\tTeam\tSubjects")
		print("{}\t{}\t{}",format(self._matricula,self._name, self._team, len(self._subjects)))
		print("")


	#Editar Email
	#Editar Senha
	#Editar Phone

class Exercises(object):

	def __init__(self):
		self._status = False	#Visibilidade do exercicio
		self._questions = {}	#PDF Texto
		self._solutions = {}	#Arquivo de Saida
		self._timeSec = {}		#Time limite de execucao

	#Cadastrar Questoẽs
	#Alterar time de um exercicio

class Subject(object):			#Disciplina
	ID_subject = 0

	__slots__ = ['_Name']
	def __init__(self, Name):
		self._idSub = str(Subject.ID_subject)
		Subject.ID_subject = str(Subject.ID_subject+(randint(500,999)))

		self._name = Name
		self._teams = {}		#{ID: Nome}
		self._exercises = {}	#{ID: Exercises()}

	#Adicionar teams
	#Remover teams
	#Cadastrar Exercicio
	#Remover Exercicio
	#Alterar visibilidade do exercicio

class Teacher(object):
	Siape = 0

	__slots__ = ['_Email', '_Password', '_Name']
	def __init__(self,Email, Password, Name):
		self._siape = str(Teacher.Siape)
		Teacher.Siape = str(Teacher.Siape+1)
		self._email = str(Email)
		self._password = str(Password)
		self._name = Name
		self._subjects = {}			#Tipo class Subject

	#Cadastrar Disciplina
	def registerSubject(self):
		Name = input("Insira nome da disciplina: ")
		obj = Subject(Name)
		self._subjects[obj._idSub] = obj 	#{Id_sub: Objeto}
		return True

	#Listar Disciplina
	def showSubject(self):
		print("ID\tNome\tQtd. Teams")
		for x, y in self._subjects.items():
			print("{}\t{}\t{}",format(y._idSub, y._name, len(y._teams.keys)))
		print("")

	#Remover Disciplina
	def deleteSubject(self):
		self.showSubject()

		ID = input("Insira ID da disciplina: ")
		try:
			rm = self._subjects.pop(ID)
			print("Disciplina {} foi removida.".format(rm._name))
		except:
			print("Disciplina inixistente.")

	#Editar Disciplina

	#Editar Email e Senha