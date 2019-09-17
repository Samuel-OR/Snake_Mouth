from classes import Login
from classes import Team
from classes import Student
from classes import Exercises
from classes import Subject
from classes import Teacher
import classes as TESTE


def menuPrincipal():
	sessao = Login()
	while(1):
		print("1 - Login")
		print("2 - Cadastrar Aluno")
		print("3 - Cadastrar Professor")
		print("#4 - Listar tudo")

		print("0 - Exit")
		op = int(input("Escolha uma opção: "))
		if(op==1):
			lista = sessao.login()

			value = lista[0]
			if(value == 1):
				#MenuTeam(lista[1])
				pass
			elif value == 2:
				#MenuStudent(lista[1])
				pass
			elif value == 3:
				MenuTeacher(lista[1])
		elif(op == 2):
			sessao.registerTeacher()
		elif(op == 3):
			sessao.registerStudent()
		elif(op == 4):
			sessao.show()
		elif(op == 0):
			exit()
		else:
			print("Opção Invalida.")

def MenuTeacher(Id):
	print("1 - Registrar Disciplina")
	print("2 - Mostrar Disciplinas")
	print("3 - Deletar Disciplina")
	print("4 - Editar Disciplina")
	print("0 - Voltar")
	op = int(input("Escolha uma opção: "))
	if(op==1):
		BDteacher[Id].registerSubject()
	elif(op == 2):
		BDteacher[Id].showSubject()
	elif(op == 3):
		sessao.deleteSubject()
	else:
		print("Opção Invalida.")

	
		


if __name__ == '__main__':
	menuPrincipal()