class Teacher(object):
	Siape = 0

	__slots__ = ['_Email', '_Password', '_Name']
	def __init__(self,Email, Password, Name):
		print(Teacher.Siape)
		self._siape = str(Teacher.Siape)
		Teacher.Siape = Teacher.Siape+1
		self._email = str(Email)
		self._password = str(Password)
		self._name = Name
		self.team = {}

	#Cadastrar Disciplina
	def registerTeam(self):
		Name = input("Insira nome da disciplina: ")
		obj = Subject(Name)
		self._subjects[obj._idSub] = obj 	#{Id_sub: Objeto}
		return True

	def registerTeacher(self):

		Email = input("Digite seu email: ")
		Password = input("Digite sua senha: ")
		Name = input("Digite nome completo: ")
		obj = Teacher(Email, Password, Name)
		self._teacher[Email] = Password
		
		BDteacher[obj._siape] = obj
		print("Professor(a) {} cadastrado(a).".format(Name))
		return True
	#Editar Email e Senha